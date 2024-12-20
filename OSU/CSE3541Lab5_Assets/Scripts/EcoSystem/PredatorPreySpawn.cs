using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace ChenAmarth
{
    public class PredatorPreySpawn : MonoBehaviour
    {
        private bool DEBUGGING = true; 

        [SerializeField] GameObject predatorModel;
        [SerializeField] GameObject preyModel;
        [SerializeField] MapGenerator MapInfo;
        [Space(10)]

        // -------------------------------------- General ----------------------------------------
        [Header("General Attributes")]
        [Space(5)]

        [Tooltip("When enabled, creatures born and die by interaction, with traits inherited by offsprings")]
        [SerializeField] private bool enableNaturalSelection = false;

        [Tooltip("Total amount of energy produced by the bottom of the eco system")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float ecosystemTotalEnergySupply = 100f;

        [Tooltip("Interval between each predator spawn, in ms")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(_NotNaturalSelection))]
        [Range(0f, 100f)]
        [SerializeField] private float predatorSpwanInterval = 3f;

        [Tooltip("Interval between each prey spawn, in ms")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(_NotNaturalSelection))]
        [Range(0f, 100f)]
        [SerializeField] private float preySpawnInterval = 1f;

        [SerializeField] private int initialPredatorNumer = 3;
        [SerializeField] private int initialPreyNumber = 6;

        [Tooltip("Distance threshold below which kill counts")]
        [SerializeField] private float killDistance = .5f;

        [Tooltip("How long a prey could live, negative will make it immortal")]
        [SerializeField] private float preyLifeSpan = -1; 

        [Tooltip("How long a predator could live, negative will make it immortal")]
        [SerializeField] private float predatorLifeSpan = 20;

        [Tooltip("If enabled, then a prey can be ate by several predators, until completely consumed. " +
            "If disabled, predator instantly gains the energy of the prey")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private bool enableGroupFeast= false;

        [Space(10)]

        // --------------------------------------------------------------------------------------
        // ------------------------------------- Predator ---------------------------------------
        [Header("Predator Base Attributes")]
        [Space(5)]

        [Tooltip("Default movement during action for predator")]
        [SerializeField] private float predatorSpeed = .1f;

        [Tooltip("During leisure, predator moves slower, this arttribute decides how much slower they move")]
        [Range(0f, 1f)]
        [SerializeField] private float predatorLeisureSpeedRatio = .5f; 

        [Tooltip("Furthurest distance that a predator could sense")]
        [SerializeField] private float predatorVisionRange = 3f;

        [Tooltip("The frontal cone angle, in which a prey could be sensed")]
        [SerializeField] private int frontConeAngle = 120;

        [Tooltip("Maxmium turnrate for a predator")]
        [SerializeField] private float predatorTurnRate = 1f;

        [Tooltip("When set to higher than 0, predator would try to predict where the prey would be")]
        [SerializeField] private float predictLead = .1f; 

        [Tooltip("During leisure, a predator makes less drastic turn than in action")]
        [Range(0f, 1f)]
        [SerializeField] private float predatorLeisureTurnMultiplier = .5f;

        [Tooltip("During leisure, predators make turns periodically, random walk")]
        [SerializeField] private float predatorRandomInterval = 1f;

        [Tooltip("During leisure, each period of random walk last slightly different time")]
        [SerializeField] private float predatorIntervalVariance = .5f;

        [Tooltip("Predators will try not to bump onto each other, note that if this value is higher than" +
            " vision range, then predator will not have flocking behavior no matter what. And if it's" +
            " equal or lower to 0, it's viewed as turned off")]
        [SerializeField] private float predatorRepusiveRange = 1f;

        [Tooltip("If enabled, predators will try to act as a group")]
        [SerializeField] private bool enablePredatorFlocking = false;

        [Tooltip("Decides how heavily predators affect each other")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enablePredatorFlocking))]
        [Range(0f, 10f)]
        [SerializeField] private float predatorFlockingWeight = .4f;

        [Tooltip("Flocking is also triggered when units are wihtin certain range. " +
            "Calculated as vision range times this ratio")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enablePredatorFlocking))]
        [Range(0f, 1f)]
        [SerializeField] private float predatorFlockingSight = .5f; 

        [Tooltip("Controls if a predator could pounce upon a target prey")]
        [SerializeField] private bool enablePounce = false;

        [Tooltip("Whether or not the predator could have a burst of speed approching the prey")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enablePounce))]
        [Range(1f, 2f)]
        [SerializeField] private float pounceSpeedMultiplier = 1.5f;

        [Tooltip("How long a pounce would last")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enablePounce))]
        [SerializeField] private float pounceLastingTime = .5f;

        [Tooltip("When natural selection is enabled, let childs mutate from parent")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private bool enablePredatorMutation = false;

        [Tooltip("How much offspring could mutate from parent")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection), nameof(enablePredatorMutation))]
        [Range(0f, 1f)]
        [SerializeField] private float predatorMutationRange = .3f;

        [Tooltip("Minimum energy to keep a predator to stay alive")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float predatorEnergyMin = 10;

        [Tooltip("Maxmium energy a predator could carry, higher will bring an offspring")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float predatorEnergyMax = 20;

        [Tooltip("Predator loss energy while not feeding, this decides how much energy is lost per second")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float predatorDissipateEPS = .2f;

        [Tooltip("The speed of energy gain while a predator is feeding")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float predatorIngressEPS = 1; 

        [Space(10)]

        // --------------------------------------------------------------------------------------
        // -------------------------------------- Prey ------------------------------------------
        [Header("Prey Base Attributes")]
        [Space(5)]

        [Tooltip("Default movement during action for Prey")]
        [SerializeField] private float preySpeed = .1f;

        [Tooltip("During leisure, prey moves slower, this arttribute decides how much slower they move")]
        [Range(0f, 1f)]
        [SerializeField] private float preyLeisureRatio = .5f;

        [Tooltip("Furthest distance of the vision cone for prey")]
        [SerializeField] private float preyVisionRange = 8f;

        [Tooltip("Size of the blind spot looking back")]
        [SerializeField] private int backBlindSpotAngle = 90;

        [Tooltip("Maxmium turn rate for prey")]
        [SerializeField] private float preyTurnRate = 1f;

        [Tooltip("During leisure, a prey makes less drastic turn than in action. " +
            "This attribute is also used to accelerate turning when being chased")]
        [Range(0f, 1f)]
        [SerializeField] private float preyLeisureTurnMultiplier = .2f;

        [Tooltip("Prey peridically changes direction, this variable decides how long a period is")]
        [SerializeField] private float preyRandomInterval = 3f;

        [Tooltip("Variance of the length of each period")]
        [SerializeField] private float preyIntervalVariance = 1f;

        [Tooltip("When bigger than 0, preys shall try to evade each other when getting too close")]
        [SerializeField] private float preyRepulsiveRange = 2f; 

        [Tooltip("When enabled, preys shall try to stick together")]
        [SerializeField] private bool enablePreyFlocking = false;

        [Tooltip("decides how heavily a prey is affected by others")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enablePreyFlocking))]
        [SerializeField] private float preyFlockingWeight = 2f;

        [Tooltip("The prey does not need to see others in the vision cone to sense them. Others can be " +
            "sensed as long as they're within a certain range")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enablePreyFlocking))]
        [Range(0f, 1f)]
        [SerializeField] private float preyFlockingSight = .7f;

        [Tooltip("Whether or not an offspring mutates from its parent")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private bool enablePreyMutation = false;

        [Tooltip("How drastic the mutation would be")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enablePreyMutation), nameof(enableNaturalSelection))]
        [Range(0f, 1f)]
        [SerializeField] private float preyMutationRange = .3f; 

        [Tooltip("After losing sight of predator, prey won't immediately switch to leisure. This variable " +
            " decides the time needed to switch into leisure mode")]
        [SerializeField] private float preyMomentumTime = 1f; 

        [Tooltip("Minimum amount of energy to stay alive, any lower will die")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float preyEnergyMin = 10f;

        [Tooltip("Maximum amount of energy a prey could carry, higher shall spawn an offspring")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float preyEnergyMax = 20f;

        [Tooltip("While not feeding, prey loses energy slowly, EPS as Energy Per Second")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float preyDissipateEPS = .1f; 

        [Tooltip("When feeding, the amount of energy incresed per second")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float preyIngressEPS = 1f;

        [Tooltip("After starved death, body does not directly disappear, but last for a short amoung of time." +
            " Only valid during natural selection")]
        [ShowIf(ActionOnConditionFail.DisableOnly, ConditionOperator.And, nameof(enableNaturalSelection))]
        [SerializeField] private float preyBodyDecayTime = 5f; 

        // -----------------------------------------------------------------------------------
        // ----------------------------------- Privates --------------------------------------
        // -----------------------------------------------------------------------------------
        
        private List<Creature> predators = new List<Creature>();
        private List<Creature> preys = new List<Creature>();
        private int creatureCounter = 0; 

        private Vector3 predatorBirthplace;
        private Vector3 preyBirthPlace;
        private float predatorTimer;
        private float preyTimer; 

        // ====================================================================================
        // ===================================== Methods ======================================
        // ====================================================================================

        private void Start()
        {
            predatorTimer = 0;
            preyTimer = 0;

            predatorBirthplace = new Vector3(
                (.5f) * MapInfo.GetCellSize(),
                0,
                (.5f) * MapInfo.GetCellSize());
            preyBirthPlace = new Vector3(
                (MapInfo.GetMapSize() - .5f) * MapInfo.GetCellSize(),
                0,
                (MapInfo.GetMapSize() - .5f) * MapInfo.GetCellSize()
                );

            if (DEBUGGING)
            {
                
                //Vector3 offset = new Vector3(.5f, 0, .5f);

                //AddCreature(true, birthPlace);
                //AddCreature(true, birthPlace + offset);
                //AddCreature(true, birthPlace + offset + offset);
                //AddCreature(true, birthPlace - offset);

                //AddCreature(false, preyBirht);
                //AddCreature(false, preyBirht + offset);
                //AddCreature(false, preyBirht - offset * 2);
                //AddCreature(false, preyBirht - offset * 3);
                //AddCreature(false, preyBirht - offset * 4);
                //foreach (Creature pred in predators)
                //    pred.UpdateListInfo(predators, preys);
                //foreach (Creature prey in preys)
                //    prey.UpdateListInfo(predators, preys);
                    
            }

        }

        private void Update()
        {
            bool NewBorn = false;
            bool HasDeath = false;

            if (enableNaturalSelection)
            {

            }
            else
            {
                
                Vector3 Rand = new Vector3(Random.RandomRange(-1f, 1f), 0, Random.RandomRange(-1f, 1f));

                preyTimer += Time.deltaTime;
                predatorTimer += Time.deltaTime; 

                if (preyTimer > preySpawnInterval)
                {
                    preyTimer = 0;
                    AddCreature(false, preyBirthPlace + Rand);
                    NewBorn = true;
                }
                if (predatorTimer > predatorSpwanInterval)
                {
                    predatorTimer = 0;
                    AddCreature(true, predatorBirthplace + Rand);
                    NewBorn = true; 
                }
            }

            // Destroy those who should have gone 
            foreach (Creature pred in predators)
                if (!pred.IsAlive())
                    pred.DestroyBody();
            foreach (Creature prey in preys)
                if (!prey.IsAlive())
                    prey.DestroyBody();

            // Remove those who should have gone 
            if (predators.RemoveAll(x => !x.IsAlive()) > 0
                || preys.RemoveAll(x => !x.IsAlive()) > 0)
                HasDeath = true;

            // If there's a change in list, inform this change to all creatures 
            if (NewBorn || HasDeath)
            {
                foreach (Creature pred in predators)
                    pred.UpdateListInfo(predators, preys);
                foreach (Creature prey in preys)
                    prey.UpdateListInfo(predators, preys);
            }
        }


        private void AddCreature(bool IsPredator, Vector3 BirthLocation)
        {
            GameObject newCreatureModel;
            int MapSize = MapInfo.GetMapSize();
            float CellSize = MapInfo.GetCellSize(); 

            if (IsPredator)
            {
                newCreatureModel = Instantiate(predatorModel, new Vector3(0, 0, 0), Quaternion.identity);
            }
            else
            {
                newCreatureModel = Instantiate(preyModel, new Vector3(0, 0, 0), Quaternion.identity);
            }

            newCreatureModel.transform.position = BirthLocation;
            newCreatureModel.AddComponent<Creature>();
            newCreatureModel.GetComponent<Creature>().SetSelfModel(newCreatureModel);
            newCreatureModel.GetComponent<Creature>().UpdateMapInfo(MapInfo);
            newCreatureModel.GetComponent<Creature>().SetCreatureID(creatureCounter);
            //newCreatureModel.GetComponent<Creature>().UpdateListInfo(predators, preys);

            if (IsPredator)
            {
                newCreatureModel.GetComponent<Creature>().SetAsPredator(killDistance, 
                    predatorSpeed, predatorLeisureSpeedRatio,
                    predatorVisionRange, frontConeAngle,
                    predatorTurnRate, predatorLeisureTurnMultiplier, 
                    enablePounce, pounceSpeedMultiplier, pounceLastingTime, predictLead,
                    predatorRandomInterval, predatorIntervalVariance,
                    enablePredatorFlocking, predatorFlockingWeight,
                    predatorFlockingSight, predatorRepusiveRange
                    );
                newCreatureModel.GetComponent<Creature>().SetLifeSpan(predatorLifeSpan);

                predators.Add(newCreatureModel.GetComponent<Creature>()); 
            }
            else
            {
                newCreatureModel.GetComponent<Creature>().SetAsPrey(killDistance,
                    preySpeed, preyLeisureRatio, preyVisionRange, backBlindSpotAngle,
                    preyTurnRate, preyLeisureTurnMultiplier, preyRandomInterval, preyIntervalVariance, preyRepulsiveRange,
                    enablePreyFlocking, preyFlockingWeight, preyFlockingSight,
                    enablePreyMutation, preyMutationRange, preyMomentumTime,
                    preyEnergyMin, preyEnergyMax, preyDissipateEPS, preyIngressEPS, preyBodyDecayTime
                    );
                newCreatureModel.GetComponent<Creature>().SetLifeSpan(preyLifeSpan);
                newCreatureModel.transform.Rotate(new Vector3(0, -90, 0));

                preys.Add(newCreatureModel.GetComponent<Creature>()); 
            }

            creatureCounter++; 
        }

        private bool _NotNaturalSelection()
        {
            return !enableNaturalSelection; 
        }
    }
}
