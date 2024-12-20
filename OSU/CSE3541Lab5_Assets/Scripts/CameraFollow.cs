using System.Reflection;
using UnityEditor;
using System.Collections.Generic;
using System;
using System.Linq;
using UnityEngine;
using UnityEngine.InputSystem;

namespace ChenAmarth
{
    public class CameraFollow : MonoBehaviour
    {
        [SerializeField] MapGenerator mapInfo;
        [SerializeField] Camera self;

        [Space(5)]

        [SerializeField] float cameraHeight = 100; 

        private void Start()
        {
            float MapLength = mapInfo.MapLength();
            self.transform.position = new Vector3(MapLength / 2, cameraHeight, MapLength/ 2);
            self.orthographicSize = MapLength / 2; 
        }
    }
}
