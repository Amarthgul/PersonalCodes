using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

namespace ChenAmarth
{
    public class MapGenerator : MonoBehaviour
    {
        private InputAction mouseClick;
        private InputAction mousePosition;

        [SerializeField] GameObject parentObject;
        [SerializeField] Camera mainCamera; 

        [Space(4)]

        [SerializeField] private int mapSize = 3;
        [SerializeField] private float cellSize = 10;

        [SerializeField] private float mapHeightRatio = .3f; 

        private bool[,] map;

        private bool newClickSession = false; 

        public void Initilize(InputAction MC, InputAction MP)
        {
            mouseClick = MC;
            mousePosition = MP; 
        }

        private void Start()
        {
            GenerateMap();
        }

        // Update is called once per frame
        void Update()
        {
            bool NewChangeDeteced = false;

            if(mouseClick.ReadValue<float>() > 0.5)
            {
                if (!newClickSession)
                {
                    newClickSession = true;
                    Vector3 MousePosTrans = mainCamera.ScreenToWorldPoint(mousePosition.ReadValue<Vector2>());
                    if (MousePosTrans.x > 0 && MousePosTrans.z > 0
                        && MousePosTrans.x < mapSize * cellSize && MousePosTrans.z < mapSize * cellSize)
                    {
                        int iLoc = Mathf.FloorToInt(MousePosTrans.x / cellSize);
                        int jLoc = Mathf.FloorToInt(MousePosTrans.z / cellSize);
                        map[iLoc, jLoc] = !map[iLoc, jLoc];
                        NewChangeDeteced = true; 
                    }
                }
                else { }
            }
            else
            {
                newClickSession = false;
            }

            if (NewChangeDeteced)
                UpdateMap();

        }


        public float MapLength()
        {
            return mapSize * cellSize; 
        }

        public int GetMapSize()
        {
            return mapSize; 
        }

        public float GetCellSize()
        {
            return cellSize; 
        }

        /// <summary>
        /// Examine if a given location is a valid place to stay in.
        /// i.e. within map and not in walls 
        /// </summary>
        /// <param name="Location">Location to examnie</param>
        /// <returns>True if within map and not in walls</returns>
        public bool IsValidPosition(Vector3 Location)
        {
            bool Result = true;
            float MapLength = mapSize * cellSize;
            int iLoc = Mathf.FloorToInt(Location.x / cellSize);
            int jLoc = Mathf.FloorToInt(Location.z / cellSize);

            if (iLoc < 0 || iLoc >= mapSize || jLoc < 0 || jLoc >= mapSize)
                Result = false;
            else
            {
                Result &= (Location.x > 0 && Location.z > 0);
                Result &= (Location.x < MapLength && Location.z < MapLength);
                Result &= !map[iLoc, jLoc];
            }

            return Result; 
        }

        // -----------------------------------------------------------------------------------
        // ----------------------------------- Privates --------------------------------------
        // -----------------------------------------------------------------------------------

        /// <summary>
        /// Generate a black map
        /// </summary>
        private void GenerateMap()
        {

            map = new bool[mapSize, mapSize];

            for (int i = 0; i < mapSize; i++)
            {
                for(int j = 0; j < mapSize; j++)
                {
                    map[i, j] = false; 
                }
            }

            UpdateMap();
        }


        /// <summary>
        /// Whenever modifications are made, update the map with this method 
        /// </summary>
        private void UpdateMap()
        {
            // First destroy all previous objects 
            for(int i = 0; i < parentObject.transform.childCount; i++)
            {
                Destroy(parentObject.transform.GetChild(i).gameObject);
            }


            // Then create new ones 
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    GameObject terrainUnit; 
                    if (map[i, j])
                    {
                        terrainUnit = GameObject.CreatePrimitive(PrimitiveType.Cube);
                        terrainUnit.transform.localScale = new Vector3(
                            cellSize, 
                            cellSize * mapHeightRatio, 
                            cellSize);
                        terrainUnit.GetComponent<Renderer>().material.SetColor("_Color", new Color(.7f, .7f, .7f));
                    }
                    else
                    {
                        // Plane has a basic length of 10
                        float planeScaleRatio = cellSize / 10f; 
                        terrainUnit = GameObject.CreatePrimitive(PrimitiveType.Plane);
                        terrainUnit.transform.localScale = new Vector3(planeScaleRatio, planeScaleRatio, planeScaleRatio);
                    }
                    terrainUnit.transform.position = new Vector3((i + .5f) * cellSize, 0, (j + .5f) * cellSize);
                    
                    terrainUnit.transform.parent = parentObject.transform; 
                }
            }
        }


    }
}
