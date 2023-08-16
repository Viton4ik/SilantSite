// malfunction_node elements
const malfunctionNodeFilter = document.querySelector("#malfunction_node");
const malfunctionNodeRowName = document.querySelector("#malfunctionNodeRowName");
const malfunctionNodeRow = document.querySelectorAll(".malfunctionNodeRow");
// malfunction_node filter
filterHandler (malfunctionNodeFilter, malfunctionNodeRowName, malfunctionNodeRow)

// reparing_method elements
const reparingMethodFilter = document.querySelector("#reparing_method");
const reparingMethodRowName = document.querySelector("#reparingMethodRowName");
const reparingMethodRow = document.querySelectorAll(".reparingMethodRow");
// reparing_method filter
filterHandler (reparingMethodFilter, reparingMethodRowName, reparingMethodRow)

// service_company elements
const serviceCompanylFilter = document.querySelector("#service_company");
const serviceCompanyRowName = document.querySelector("#serviceCompanyRowName");
const serviceCompanyRow = document.querySelectorAll(".serviceCompanyRow");
// service_company filter
filterHandler (serviceCompanylFilter, serviceCompanyRowName, serviceCompanyRow)

// buttons elements
const resetButtonFilterMain = document.querySelector("#resetButtonFilterMain");
const buttonApplyFilterMain = document.querySelector("#buttonApplyFilterMain");


// reset button handler
resetButtonFilterMain.addEventListener("click", function() {
    malfunctionNodeFilter.value = ''
    reparingMethodFilter.value = ''
    serviceCompanylFilter.value = ''
    buttonApplyFilterMain.click()
});

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


