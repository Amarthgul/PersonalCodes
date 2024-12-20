using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace ChenAmarth
{
    public class creatureStructs : MonoBehaviour
    {
        struct PredatorStats
        {
            float killDistance;
            float predatorSpeed;
            float predatorLeisureSpeedRatio;
            float predatorVisionRange; 
            int frontConeAngle; 
            float predatorTurnRate; 
            float predatorLeisureTurnMultiplier;

            bool enablePounce; 
            float pounceSpeedMultiplier; 
            float pounceLastingTime; 

            float predictLead;

            float predatorRandomInterval; 
            float predatorIntervalVariance; 

            bool enablePredatorFlocking; 
            float predatorFlockingWeight; 
            float predatorFlockingSight;

            float predatorRepusiveRange;
        }
    }
}
