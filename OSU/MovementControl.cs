using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

namespace ChenAmarth
{
    public class MovementControl : MonoBehaviour
    {

        private bool DEBUG = true;

        private InputAction moveAction;

        [SerializeField] private GameObject ObjectToOperate;
        [SerializeField] private GameObject RollChild;
        [SerializeField] private GameObject PitchChild;

        [SerializeField] private ChargeHandler chargeHandler;

        

        // ----------------------- Translate -------------------------
        [Header("Movement")]
        [Space(5)]
        [Tooltip("How fast the character reaches max speed.")]
        [SerializeField] private float acceleration = .01f;

        [Tooltip("Maximum speed forward.")]
        [SerializeField] private float maxSpeedForward = .1f;  // Unsigned
        
        [Tooltip("Maximum speed backward.")]
        [SerializeField] private float maxSpeedBackward = .1f; // Unsigned 

        [Tooltip("Ratio of how much faster character becomes when charging.")]
        [SerializeField] private float ChargeMultiplier = 1.5f;

        [Tooltip("When checked, character gradually go back to still if no movement key is pressed.")]
        [SerializeField] private bool enableMovementFalloff = true;

        [Tooltip("How fast the cahracter becoes still after move key is released.")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableMovementFalloff))]
        [Range(0f, 1f)]
        public float movementFallOffRatio = .85f;

        [Space(20)]

        private float currentSpeed = 0f;


        // ------------------------ Rotate ---------------------------
        [Header("Turn and rotate")]
        [Space(5)]

        [Tooltip("Same as the naval term \"meet her\"")]
        [SerializeField] private bool autoStabilize = true;

        [Tooltip("How fast the character stops turning after turn key is released.")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(autoStabilize))]
        [Range(0f, 1f)]
        public float restabilizeRatio = .85f;

        [Tooltip("When checked, character rolls when turning, affected by turn rate.")]
        [SerializeField] private bool enableRoll = true;  

        [Tooltip("Maximum angle of roll effect.")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableRoll))]
        [Range(0f, 90f)]
        public float rollMaxAngle = 7.5f;

        [Tooltip("When checked, character pitches with speed, affected by movement spped.")]
        [SerializeField] private bool enablePitch = true; 

        [Tooltip("Maximum angle of pitch effect.")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enablePitch))]
        [Range(0f, 90f)]
        public float pitchMaxAngle = 7.5f;

        [Tooltip("How fast the character turns")]
        public float turnAcceleration = .1f;

        [Tooltip("Maximum speed of turning")]
        [SerializeField] private float maxTurnRate = 1.5f; 

        private float currentTurn = 0f;
        private float currentRoll = 0f;
        private float currentPitch = 0f;

        private float pitchChargingModifier = .2f; // Avoid over turn 
        

        public void Initialize(InputAction MA)
        {
            moveAction = MA;
            moveAction.Enable();
        }

        /// <summary>
        /// Whether or not the current speed is not zero.
        /// </summary>
        /// <returns>True is speed is non zero</returns>
        public bool IsMoving()
        {
            return currentSpeed > 0 || currentSpeed < 0; 
        }

        private void FixedUpdate()
        {
            ResetStats();

            CalculateRotate();
            CalculateMove();

            ApplyCalculations();

        }

        /// <summary>
        /// Reset necessary stats
        /// </summary>
        private void ResetStats()
        {

        }

        /// <summary>
        /// Calculate rotation related paras.
        /// Including main rotation, roll, and pitch
        /// </summary>
        private void CalculateRotate()
        {

            if (moveAction.ReadValue<Vector2>().x > 0)
            {
                currentTurn += turnAcceleration;
            }
            else if (moveAction.ReadValue<Vector2>().x < 0)
            {
                currentTurn -= turnAcceleration;
            }
            else
            {
                if (autoStabilize)
                {
                    if (Mathf.Abs(currentTurn) < turnAcceleration)
                    {
                        currentTurn = 0;
                    }
                    else
                    {
                        currentTurn = Mathf.Sign(currentTurn) * (Mathf.Abs(currentTurn) - turnAcceleration * restabilizeRatio);
                    }
                }
            }

            // Clamp max turn rate
            if (Mathf.Abs(currentTurn) > maxTurnRate)
            {
                currentTurn = Mathf.Sign(currentTurn) * maxTurnRate;
            }

            currentRoll = Mathf.Sign(currentTurn) * rollMaxAngle * (Mathf.Abs(currentTurn) / maxTurnRate);
            currentRoll *= (Mathf.Abs(currentSpeed) / maxSpeedForward);  // No effect when staying still 

        }

        /// <summary>
        /// Calculate movement updates 
        /// </summary>
        private void CalculateMove()
        {
            bool CurrentCharging = chargeHandler.IsCharging();
            float CurrentAcceleration = acceleration * (CurrentCharging ? ChargeMultiplier : 1f); 
            Debug.Log("current is " + CurrentCharging + " accele at " + CurrentAcceleration);

            if (moveAction.ReadValue<Vector2>().y > 0)
            {
                currentSpeed += CurrentAcceleration;
            }    
            else if (moveAction.ReadValue<Vector2>().y < 0)
            {
                currentSpeed -= CurrentAcceleration;
            }
            else
            {
                if (enableMovementFalloff)
                {
                    if (Mathf.Abs(currentSpeed) <= acceleration * movementFallOffRatio)
                    {
                        currentSpeed = 0;
                    }
                    else // Gradually decrease speed
                    {
                        currentSpeed = Mathf.Sign(currentSpeed) * (Mathf.Abs(currentSpeed) - acceleration * movementFallOffRatio);
                    }
                }
            }

            float currentMaxFront = maxSpeedForward * (CurrentCharging ? ChargeMultiplier : 1f);
            float currentMaxBack = maxSpeedBackward * (CurrentCharging ? ChargeMultiplier : 1f);
            // Clamp max speed 
            if (currentSpeed > currentMaxFront)
            {
                currentSpeed = currentMaxFront;
            }
            if (currentSpeed < -currentMaxBack)
            {
                currentSpeed = -currentMaxBack;
            }

            currentPitch = Mathf.Sign(currentSpeed) * pitchMaxAngle * (Mathf.Abs(currentSpeed) / maxSpeedForward);

            currentPitch *= (CurrentCharging ? (1 + ChargeMultiplier * pitchChargingModifier) : 1f);
        }

        /// <summary>
        /// Conditionally apply selected transform onto the object and its children
        /// </summary>
        private void ApplyCalculations()
        {
            //if (DEBUG) Debug.Log("Moving at \t" + currentSpeed);

            ObjectToOperate.transform.Rotate(0, currentTurn, 0, Space.Self);

            ObjectToOperate.transform.position += ObjectToOperate.transform.forward * currentSpeed;

            if (enablePitch)
            {
                PitchChild.transform.localRotation = Quaternion.Euler(currentPitch, 0, 0);
            }

            if (enableRoll)
            {
                RollChild.transform.localRotation = Quaternion.Euler(0, 0, currentRoll);
            }

        }
    }
}
