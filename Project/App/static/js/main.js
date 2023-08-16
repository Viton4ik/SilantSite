// vehicle elements
const vehicleModelFilter = document.querySelector("#vehicle_model");
const vehicleModelRowName = document.querySelector("#vehicleModelRowName");
const vehicleModelRow = document.querySelectorAll(".vehicleModelRow");

// engine elements
const engineModelFilter = document.querySelector("#engine_model");
const engineModelRowName = document.querySelector("#engineModelRowName");
const engineModelRow = document.querySelectorAll(".engineModelRow");

// transmission elements
const transmissionModelFilter = document.querySelector("#transmission_model");
const transmissionModelRowName = document.querySelector("#transmissionModelRowName");
const transmissionModelRow = document.querySelectorAll(".transmissionModelRow");

// driveAxle elements
const driveAxleModelFilter = document.querySelector("#driveAxle_model");
const driveAxleModelRowName = document.querySelector("#driveAxleModelRowName");
const driveAxleModelRow = document.querySelectorAll(".driveAxleModelRow");

// steeringAxle elements
const steeringAxleModelFilter = document.querySelector("#steeringAxle_model");
const steeringAxleModelRowName = document.querySelector("#steeringAxleModelRowName");
const steeringAxleModelRow = document.querySelectorAll(".steeringAxleModelRow");

// buttons elements
const resetButtonFilterMain = document.querySelector("#resetButtonFilterMain");
const buttonApplyFilterMain = document.querySelector("#buttonApplyFilterMain");


// reset button handler
resetButtonFilterMain.addEventListener("click", function() {
    vehicleModelFilter.value = ''
    engineModelFilter.value = ''
    transmissionModelFilter.value = ''
    driveAxleModelFilter.value = ''
    steeringAxleModelFilter.value = ''
    buttonApplyFilterMain.click()
});

// highlight elements if filters have been set
// vehicle filter
if (vehicleModelFilter.value !== '') {
    // row name
    vehicleModelRowName.style.border = '2px solid #D20A11'; 
    // each element in the row
    vehicleModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11'; 
    });
} 
// engine filter
if (engineModelFilter.value !== '') {

    engineModelRowName.style.border = '2px solid #D20A11'; 

    engineModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11'; 
    });
} 
// transmission filter
if (transmissionModelFilter.value !== '') {

    transmissionModelRowName.style.border = '2px solid #D20A11'; 

    transmissionModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11'; 
    });
} 
// driveAxle filter
if (driveAxleModelFilter.value !== '') {

    driveAxleModelRowName.style.border = '2px solid #D20A11'; 

    driveAxleModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11'; 
    });
} 
// steeringAxle filter
if (steeringAxleModelFilter.value !== '') {

    steeringAxleModelRowName.style.border = '2px solid #D20A11'; 

    steeringAxleModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11'; 
    });
} 




// vehicleModelFilter.addEventListener("change", function() {
//     if (vehicleModelFilter.value !== '') {
//         vehicleModelRow.style.border = '2px solid #D20A11'; 
//         vehicleModelRow_.style.border = '2px solid #D20A11'; 
//         // vehicleModelRow.classList.add("vehicleModelRow");
//     } 
//     // else {
//     // vehicleModelRow.style.border = 'none';
//     // }

// });



// buttonApplyFilterMain.addEventListener("click", function() {
//     if (vehicleModelFilter.value !== '') {
//         vehicleModelRow.style.border = '2px solid #D20A11'; 
//         vehicleModelRow_.style.border = '2px solid #D20A11'; 
//     } 
//     // else {
//     // vehicleModelRow.style.border = 'none';
//     // }

// });




    // // API handler
    // // retrieve the existing object from the server
    // fetch(`http://127.0.0.1:8000/chat/api-auth/room/${button.id}/`)
    // .then(response => response.json())
    // .then(object => {
    //     // modify the necessary attribute value
    //     // object.name = prompt(`new a name for the room '${object.name}'`)
    //     object.name = newRoomName
    //     // refresh the name of the room on the page
    //     roomNameDisplay.textContent = `'${newRoomName}'`
    //     // send the updated object back to the server
    //     fetch(`http://127.0.0.1:8000/chat/api-auth/room/${button.id}/`, {
    //     method: 'PUT',
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'X-CSRFToken': csrf_token(),
    //     },
    //     body: JSON.stringify(object),
    //     })
    //     .then(response => {
    //     if (response.ok) {
    //         console.log('Object updated successfully')
    //         // refresh the page
    //         // location.reload()
    //     } else {
    //         console.log('Object update failed')
    //     }
    //     })
    //     .catch(error => console.log('Error:', error))
    // })
    // .catch(error => console.log('Error:', error))