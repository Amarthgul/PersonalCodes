using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

namespace ChenAmarth
{
    public class InputManager : MonoBehaviour
    {
        
        [SerializeField] private MapGenerator mapGenerator;
        //[SerializeField] private CameraFollow cameraControl;
        //[SerializeField] private ChargeHandler chargeHandler; 

        private PlayerInput inputScheme;

        private void Awake()
        {
            inputScheme = new PlayerInput();

            mapGenerator.Initilize(inputScheme.Player.MouseLMB, inputScheme.Player.MousePosition);
            
        }

        private void OnEnable()
        {
            inputScheme.Enable();

            var _q = new QuitHandler(inputScheme.Player.Quit);

        }

        
    }
}
