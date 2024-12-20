using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using System.Diagnostics;


namespace ChenAmarth
{
    public class ChargeHandler : MonoBehaviour
    {
        [SerializeField] private MovementControl primaryMovement; 
        [SerializeField] private Texture2D[] speedLines;

        [SerializeField] private bool enableCharge = false;

        private InputAction charge;

        private Stopwatch stopwatch = new Stopwatch();
        private int imageIndex = 0;
        private int imageInterval = 100;
        private int randRange = 25;

        private int nextInterval; 

        public void Initialize(InputAction CA)
        {
            charge = CA;

            stopwatch.Start();
            RefreshNextInterval();
        }

        void Update()
        {
            UnityEngine.Debug.Log("Next interval " + nextInterval + " at image " + imageIndex);
        }

        void OnGUI()
        {
            if (enableCharge && IsCharging() && primaryMovement.IsMoving())
            {
                if(stopwatch.ElapsedMilliseconds > nextInterval)
                {
                    stopwatch.Restart();
                    imageIndex++;
                    RefreshNextInterval();
                }
                GUI.DrawTexture(new Rect(0, 0, Screen.width, Screen.height), speedLines[imageIndex % speedLines.Length]);
            }
        }

        public bool IsCharging()
        {
            return charge.ReadValue<float>() > .5;
        }

        private void RefreshNextInterval()
        {
            nextInterval = Random.Range(imageInterval - randRange, imageInterval + randRange);
        }
    }
}
