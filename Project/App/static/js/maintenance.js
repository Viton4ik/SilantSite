// maintenance_type elements
const maintenanceTypeFilter = document.querySelector("#maintenance_type");
const maintenanceTypeRowName = document.querySelector("#maintenanceTypeRowName");
const maintenanceTypeRow = document.querySelectorAll(".maintenanceTypeRow");

// vehicle_number elements
const vehicleNumberFilter = document.querySelector("#vehicle_number");
const vehicleNumberRowName = document.querySelector("#vehicleNumberRowName");
const vehicleNumberRow = document.querySelectorAll(".vehicleNumberRow");

// service_company elements
const serviceCompanylFilter = document.querySelector("#service_company");
const serviceCompanyRowName = document.querySelector("#serviceCompanyRowName");
const serviceCompanyRow = document.querySelectorAll(".serviceCompanyRow");

// buttons elements
const resetButtonFilterMain = document.querySelector("#resetButtonFilterMain");
const buttonApplyFilterMain = document.querySelector("#buttonApplyFilterMain");


// reset button handler
resetButtonFilterMain.addEventListener("click", function() {
    maintenanceTypeFilter.value = ''
    vehicleNumberFilter.value = ''
    serviceCompanylFilter.value = ''
    buttonApplyFilterMain.click()
});

// highlight elements if filters have been set
// maintenance_type filter
filterHandler (maintenanceTypeFilter, maintenanceTypeRowName, maintenanceTypeRow)

// vehicle_number filter
filterHandler (vehicleNumberFilter, vehicleNumberRowName, vehicleNumberRow)

// service_company filter
filterHandler (serviceCompanylFilter, serviceCompanyRowName, serviceCompanyRow)


//filter handler function
function filterHandler (filter, rowName, row) {
    if (filter.value !== '') {
        // row name
        rowName.style.border = '2px solid #D20A11'; 
        // each element in the row
        row.forEach((element) => {
            element.style.border = '2px solid #D20A11'; 
        });
    } 
}
