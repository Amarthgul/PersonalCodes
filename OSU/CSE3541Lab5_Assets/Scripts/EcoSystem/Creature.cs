using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace ChenAmarth
{
    /// <summary>
    /// Leisure: prey is feeding. 
    /// Escaping: prey noticed a predator and is trying to escape.
    /// Ate: Prey has been capture and is being eaten. 
    /// </summary>
    enum PreyStates {Leisure, Escaping, Ate};
    enum PredatorStates {Leisure, Chasing, Feeding };

    public class Creature : MonoBehaviour
    {
        private const float UNCOUPLING = 0.9f; // Avoid completeky stuck  

        private const bool SHOW_VISION_RANGE = true;
        private const float VISION_BEAM_THICKNESS = .1f; 

        private GameObject self;
        private MapGenerator mapInfo;

        public List<Creature> predatorList = new List<Creature>();
        public List<Creature> preyList = new List<Creature>();

        // -------------------------- Basic stats --------------------------
        private int selfID;
        private bool isPredator = false;

        private float killDistance;

        private float lifeSpan;
        private bool isImmortal; 

        // ------------------------- Move and turn -------------------------
        private float moveSpeed = 5f;
        private float leisireSpeedRatio = .5f; 
        private float turnRate = 1f;

        private float leisureTurnRateMultiplier = .5f; 
        private float randomUpdateInterval = 1f;
        private float intervalVariance = .5f;

        private float predictLead; 

        private bool enablePounce;
        private bool pounceSession; 
        private float pounceMulti;
        private float pounceTime;
        private float pounceTimer; 

        private float currentTime;
        private float currentTurnRate;
        private Vector3 currentMovement;

        // --------------------------- Vision ----------------------------
        private float visionRange = 2f;
        private int frontConeAngle = 90;

        // -------------------------- Behavior ---------------------------
        private bool enableFlocking;
        private float flockingWeight; // How much an indiduval is affected by the flock
        private float flockingVisionRatio; 

        private float repulsiveRange;

        // --------------------- Natural selection -----------------------
        private bool enableNaturalSelection;
        private bool enableMutation;
        private float mutationRange;

        private float energyMin;
        private float energyMax;
        private float energyDissipateEPS;
        private float energyIngressEPS;
        private float bodyDecayTime; 

        // --------------------- States and target -----------------------
        private PredatorStates predatorState;
        private PreyStates preyState;
        private Creature target;

        private float preyMomentumTime;      // Group fileds for preys' momentum 
        private bool momentumCheckingPeriod;
        private float momentumCheckingTimer; 

        private bool exist;    

        public Creature(bool IsPredator)
        {
            isPredator = IsPredator;
            currentTime = randomUpdateInterval;
            currentTurnRate = 0;
            lifeSpan = 0; 
            predatorList = new List<Creature>();
            preyList = new List<Creature>();

            momentumCheckingPeriod = false; 

            exist = true; 
        }

        /// <summary>
        /// Mark a creature as predator, given all value needed
        /// </summary>
        public void SetAsPredator(float KD, float MS, float LSR,
            float VR, int FC, float TR, float LTM,
            bool EP, float PM, float PT, float PL,
            float RUI, float IV, bool EF, float PFW, float FVR,
            float RR)
        {
            isPredator = true;
            pounceSession = false;
            exist = true;

            killDistance = KD;

            moveSpeed = MS;
            leisireSpeedRatio = LSR; 
            visionRange = VR;
            frontConeAngle = FC;
            turnRate = TR;
            leisureTurnRateMultiplier = LTM; 

            enablePounce = EP;
            pounceMulti = PM;
            pounceTime = PT;
            predictLead = PL; 

            randomUpdateInterval = RUI;
            intervalVariance = IV;

            enableFlocking = EF;
            flockingWeight = PFW;
            flockingVisionRatio = FVR;
            repulsiveRange = RR;

            predatorState = PredatorStates.Leisure;
            CreateVisionConesPredator();
        }
        /// <summary>
        /// Mark a creature as prey 
        /// </summary>
        public void SetAsPrey(float KD, float PS, float PLR, float PVR, int BLSA,
            float PTR, float PLTR, float PRI, float PIV, float PRR,
            bool EPF, float PFW, float PFS, 
            bool EM, float PMR, float PMT,
            float PEMin, float PEMax, float PDE, float PIE, float PBDT)
        {
            isPredator = false;
            exist = true;

            killDistance = KD;

            moveSpeed = PS;
            leisireSpeedRatio = PLR;
            visionRange = PVR;
            frontConeAngle = 360 - BLSA;
            turnRate = PTR;
            leisureTurnRateMultiplier = PLTR;
            randomUpdateInterval = PRI;
            intervalVariance = PIV;
            enableFlocking = EPF;
            flockingWeight = PFW;
            flockingVisionRatio = PFS;
            repulsiveRange = PRR; 
            enableMutation = EM;
            mutationRange = PMR;
            preyMomentumTime = PMT; 

            energyMin = PEMin;
            energyMax = PEMax;
            energyDissipateEPS = PDE;
            energyIngressEPS = PIE;
            bodyDecayTime = PBDT; 

            preyState = PreyStates.Leisure;
            CreateVisionConesPrey();
        }
        public void SetCreatureID(int ID)
        {
            selfID = ID;
        }
        public void SetSelfModel(GameObject Model)
        {
            self = Model; 
        }
        public void SetLifeSpan(float LS)
        {
            lifeSpan = LS;
            if (LS <= 0)
                isImmortal = true;
            else
                isImmortal = false;
        }
        public void UpdateMapInfo(MapGenerator MapInfo)
        {
            mapInfo = MapInfo;
        }
        public void UpdateListInfo(List<Creature> Predators, List<Creature> Preys)
        {
            predatorList = Predators;
            preyList = Preys; 
        }
        public Vector3 GetPosition()
        {
            return self.transform.position; 
        }
        public Quaternion GetRotation()
        {
            return self.transform.rotation; 
        }
        public Vector3 GetForward()
        {
            return self.transform.forward; 
        }
        public float GetLiftSpan()
        {
            return lifeSpan;
        }
        public int GetID()
        {
            return selfID; 
        }
        public bool IsAlive()
        {
            return exist; 
        }
        public bool IsPredator()
        {
            return isPredator; 
        }
        public void MarkAsDead()
        {
            if (!isPredator)
            {
                if (enableNaturalSelection)
                {

                }
                else
                {
                    exist = false;
                }
            }
            else
            {
                exist = false;
            }
        }
        public void DestroyBody()
        {
            Destroy(self);
        }
        
        private void Update()
        {
            if (!exist) return;

            if (!isImmortal)
            {
                lifeSpan -= Time.deltaTime;
                if (lifeSpan < 0)
                    MarkAsDead(); 
            }
                

            if (isPredator)
                UpdatePredator();
            else
                UpdatePrey();

        }

        // -----------------------------------------------------------------------------------
        // ----------------------------------- Privates --------------------------------------
        // -----------------------------------------------------------------------------------

        private void UpdatePredator()
        {
            

            switch (predatorState)
            {
                case PredatorStates.Chasing:
                    UpdateChasingPrey();
                    break;
                case PredatorStates.Feeding:
                    break;
                case PredatorStates.Leisure:
                    UpdateLeisure();
                    CheckForPredatorPrey();
                    break;
                default: break; 
            }

            
        }

        private void UpdatePrey()
        {
            switch (preyState)
            {
                case PreyStates.Ate:
                    break;
                case PreyStates.Escaping:
                    UpdateEscapingFromPredator();
                    break;
                case PreyStates.Leisure:
                    UpdateLeisure();
                    CheckForPredatorPrey();
                    break;
                default: break;
            }
        }

        private void UpdateFlockingAndRepulsive()
        {
            List<Creature> Others = isPredator? predatorList : preyList;

            if (Others.Count == 0) return; 

            foreach(Creature other in Others)
            {
                Vector3 TargetPosition = other.GetPosition();
                float TargetDistance = Vector3.Distance(TargetPosition, self.transform.position); 
                if (other.GetID() != selfID)
                {
                    // Repusive force 
                    if (TargetDistance < repulsiveRange)
                    {
                        float RepulsiveWeight = 1 - Mathf.Clamp(TargetDistance / repulsiveRange, 0f, 1f); 
                        Vector3 RepusiveDirection = TargetPosition - self.transform.position;

                        // First accelerate or deaccelerate the movement speed 
                        float ForwardModifier = Mathf.Sign(Vector3.Dot(RepusiveDirection, self.transform.forward));
                        currentMovement -= currentMovement * ForwardModifier * RepulsiveWeight * UNCOUPLING;

                        // Then turn to the other direction
                        Vector3 RightDirection = Vector3.Cross(self.transform.forward, Vector3.up);
                        float DirectionModifier = Mathf.Sign(Vector3.Dot(RepusiveDirection, RightDirection));
                        currentTurnRate *= -DirectionModifier; 
                    }

                    // flocking behavior 
                    if (enableFlocking && 
                        (TargetDistance <= visionRange * flockingVisionRatio || TargetInCone(TargetPosition)))  
                    {
                        self.transform.rotation = Quaternion.RotateTowards(self.transform.rotation,
                            other.GetRotation(), flockingWeight * Time.deltaTime);
                    }
                }

                
            }
        }

        /// <summary>
        /// Prey check for predators, predators check for prey
        /// </summary>
        private void CheckForPredatorPrey()
        {
            List<Creature> Others = isPredator ? preyList : predatorList;

            foreach (Creature other in Others)
            {
                Vector3 TargetPosition = other.GetPosition();

                if (TargetInCone(TargetPosition))
                {
                    if (isPredator)
                    {
                        predatorState = PredatorStates.Chasing;

                        if (enablePounce)
                        {
                            pounceSession = true;
                            pounceTimer = 0;
                        }
                    }
                    else
                    {
                        preyState = PreyStates.Escaping;
                        momentumCheckingPeriod = false;
                        momentumCheckingTimer = 0;
                    }
                    target = other;
                    return; 
                }
            }
        }

        /// <summary>
        /// General method for cretures in their leisure state
        /// </summary>
        private void UpdateLeisure()
        {
            currentMovement = self.transform.forward * moveSpeed * Time.deltaTime * leisireSpeedRatio;
            float LeisureRotation = currentTurnRate; 

            currentTime -= Time.deltaTime;
            if (currentTime < 0)
            {
                currentTime = randomUpdateInterval + (Random.Range(-100, 100) / 100f) * intervalVariance;
                currentTurnRate = leisureTurnRateMultiplier * turnRate 
                    * (Random.Range(-100, 100) / 100f) * Time.deltaTime;
                LeisureRotation = currentTurnRate; 
            }

            // Avoid hard collision with map border or walls 
            if (!mapInfo.IsValidPosition(self.transform.position + currentMovement))
            {
                currentMovement = new Vector3(0, 0, 0);
                LeisureRotation = (Mathf.Sign(currentTurnRate) * turnRate * Time.deltaTime) / leisureTurnRateMultiplier;
            }
            else
            {
                // Flocking goes before hard collision 
                // Allows soft collision with others of the same kind 
                UpdateFlockingAndRepulsive();
            }

            self.transform.position += currentMovement;
            self.transform.Rotate(new Vector3(0, LeisureRotation, 0));
        }

        /// <summary>
        /// Update method for predator in chasing state. 
        /// </summary>
        private void UpdateChasingPrey()
        {
            // If the target has alreday been eaten by someone else 
            if (target == null || !target.IsAlive())
            {
                predatorState = PredatorStates.Leisure;
                target = null;
                return; // Clear and exit
            }

            Vector3 TargetLocation = target.GetPosition() + (target.GetForward() * predictLead);

            currentMovement = self.transform.forward * moveSpeed * Time.deltaTime;

            // Check for pounce 
            Vector3 predatorMovement = currentMovement; 
            if (enablePounce && pounceSession)
            {
                predatorMovement *= pounceMulti;
                pounceTimer += Time.deltaTime;
                if (pounceTimer > pounceTime)
                    pounceSession = false; 
            }

            if (!mapInfo.IsValidPosition(self.transform.position + currentMovement))
            {
                predatorMovement = new Vector3(0, 0, 0);
            }

            UpdateCatchingPrey(TargetLocation);

            self.transform.position += predatorMovement;
            Quaternion LookAtQuaternion = Quaternion.LookRotation(TargetLocation - self.transform.position);
            self.transform.rotation = Quaternion.Slerp(self.transform.rotation, 
                LookAtQuaternion, turnRate * Time.deltaTime);
        }

        /// <summary>
        /// Update method for predator, dealing with either catching the prey or lose sight of it.
        /// </summary>
        /// <param name="TargetLocation">Location of the prey</param>
        private void UpdateCatchingPrey(Vector3 TargetLocation)
        {
            float TargetDistance = Vector3.Distance(TargetLocation, self.transform.position);

            // Capturing a target 
            if (TargetDistance < killDistance)
            {
                target.MarkAsDead();
                if (enableNaturalSelection)
                {   // In natural selection, prey left a body to be feed on 
                    predatorState = PredatorStates.Feeding;
                }
                else
                {   // In non natural selection, prey dies instantly 
                    predatorState = PredatorStates.Leisure;
                    target.MarkAsDead();
                }
            }

            // Lose sight of the target
            if (!TargetInCone(TargetLocation))
            {
                predatorState = PredatorStates.Leisure;
            }
        }

        /// <summary>
        /// Update method for prey being chased by a predator 
        /// </summary>
        private void UpdateEscapingFromPredator()
        {
            // If the predator (somehow) died during the process
            if ( target == null || !target.IsAlive())
            {
                predatorState = PredatorStates.Leisure;
                target = null;
                return;
            }

            float EscpaingRotation = currentTurnRate;

            Vector3 TargetDirection = target.transform.position - self.transform.position;
            Vector3 SelfRight = Vector3.Cross(self.transform.forward, Vector3.up);
            float TurnDirection = Mathf.Sign(Vector3.Dot(SelfRight, TargetDirection));

            currentMovement = self.transform.forward * moveSpeed * Time.deltaTime;


            // Prey peridically change dirction trying to escape 
            currentTime -= Time.deltaTime;
            if (currentTime < 0)
            {
                currentTime = (randomUpdateInterval + (Random.Range(-100, 100) / 100f) * intervalVariance)
                    * (1 - leisureTurnRateMultiplier);

                currentTurnRate = turnRate * Time.deltaTime * TurnDirection;
                EscpaingRotation = currentTurnRate; 
            }

            // If facing a wall, try turn faster 
            if (!mapInfo.IsValidPosition(self.transform.position + currentMovement))
            {
                currentMovement = new Vector3(0, 0, 0);
                EscpaingRotation = currentTurnRate / leisureTurnRateMultiplier;
            }

            UpdateEscapeDistancing();

            self.transform.position += currentMovement;
            self.transform.Rotate(new Vector3(0, EscpaingRotation, 0));
        }

        /// <summary>
        /// Update method for prey to check whether or not it have got rid of a predator 
        /// </summary>
        private void UpdateEscapeDistancing()
        {
            // If initial target predator is not visble for prey anymore 
            if (!TargetInCone(target.GetPosition()))
            {
                if (preyMomentumTime > 0)
                {
                    if (momentumCheckingPeriod)
                    {   // If over the momentum time, take it as safe
                        momentumCheckingTimer += Time.deltaTime;
                        if (momentumCheckingTimer > preyMomentumTime)
                            MarkPreyAsSafe();
                    }
                    else
                    {   // Initilize a checking period
                        momentumCheckingTimer = 0; 
                        momentumCheckingPeriod = true;
                    }
                }
                else
                {   // Without momentum, directly switch to leisure
                    MarkPreyAsSafe();
                }
            }
        }

        /// <summary>
        /// Mark a prey as safe from predators 
        /// </summary>
        private void MarkPreyAsSafe()
        {
            preyState = PreyStates.Leisure;
            target = null;
        }

        /// <summary>
        /// Quick method of judging whether or not a target is within frontal vision cone.
        /// </summary>
        /// <param name="Location">location of the target</param>
        /// <returns>True if the target is in vision cone</returns>
        private bool TargetInCone(Vector3 Location)
        {
            float TargetDistance = Vector3.Distance(Location, self.transform.position);
            if (TargetDistance < visionRange &&
                    Mathf.Abs(Vector3.Angle(Location, self.transform.position)) <= (frontConeAngle / 2))
                return true;
            else
                return false; 
        }

        /// <summary>
        /// Visualizing the visual cone by creating some beams as representation
        /// </summary>
        private void CreateVisionConesPredator()
        {
            if (!SHOW_VISION_RANGE) return; 

            int PredatorBeamCount = 7;
            int SideBeamCount = Mathf.FloorToInt(PredatorBeamCount / 2f);
            float SingleStepAngle = frontConeAngle / (PredatorBeamCount - 1f); 

            for (int i = -SideBeamCount; i <= SideBeamCount; i++)
            {
                GameObject VisionBeam = GameObject.CreatePrimitive(PrimitiveType.Cube);
                VisionBeam.transform.localScale = new Vector3(VISION_BEAM_THICKNESS, VISION_BEAM_THICKNESS, visionRange);
                VisionBeam.transform.position = self.transform.position;
                VisionBeam.transform.rotation = Quaternion.Euler(0, SingleStepAngle * i, 0);
                VisionBeam.transform.position += VisionBeam.transform.forward * visionRange / 2;
                VisionBeam.transform.parent = self.transform;
                VisionBeam.GetComponent<Renderer>().material.SetColor("_Color", new Color(1f, .5f, .5f));
                VisionBeam.GetComponent<Renderer>().material.SetColor("_EMISSION", new Color(1f, .3f, .3f));
            }
        }

        /// <summary>
        /// Visualizing the visual cone by creating some beams as representation.
        /// Prey has more beams since their angles are usually bigger. 
        /// </summary>
        private void CreateVisionConesPrey()
        {
            if (!SHOW_VISION_RANGE) return;

            int PredatorBeamCount = 17;
            int SideBeamCount = Mathf.FloorToInt(PredatorBeamCount / 2f);
            float SingleStepAngle = frontConeAngle / (PredatorBeamCount - 1f);

            for (int i = -SideBeamCount; i <= SideBeamCount; i++)
            {
                GameObject VisionBeam = GameObject.CreatePrimitive(PrimitiveType.Cube);
                VisionBeam.transform.localScale = new Vector3(VISION_BEAM_THICKNESS, VISION_BEAM_THICKNESS, visionRange);
                VisionBeam.transform.position = self.transform.position;
                VisionBeam.transform.rotation = Quaternion.Euler(0, SingleStepAngle * i, 0);
                VisionBeam.transform.position += VisionBeam.transform.forward * visionRange / 2;
                VisionBeam.transform.parent = self.transform;
                VisionBeam.GetComponent<Renderer>().material.SetColor("_Color", new Color(.5f, 1f, .5f));
                VisionBeam.GetComponent<Renderer>().material.SetColor("_EMISSION", new Color(.3f, 1f, .3f));
            }
        }
    }
}
