$(document).ready(function(){
    // Activate tooltip
    $('[data-toggle="tooltip"]').tooltip();
    
    // Select/Deselect checkboxes
    var checkbox = $('table tbody input[type="checkbox"]');
    $("#selectAll").click(function(){
        if(this.checked){
            checkbox.each(function(){
                this.checked = true;                        
            });
        } else{
            checkbox.each(function(){
                this.checked = false;                        
            });
        } 
    });
    checkbox.click(function(){
        if(!this.checked){
            $("#selectAll").prop("checked", false);
        }
    });

    // Delete selected employees
    $("#deleteSelected").click(function(){
        var selectedEmployees = [];
        $(".employee-checkbox:checked").each(function() {
            selectedEmployees.push($(this).val());
        });
        if(selectedEmployees.length > 0){
            if(confirm("Are you sure you want to delete the selected employees?")){
                $.ajax({
                    type: 'POST',
                    url: '/delete_selected/', // Update the URL here to match your DeleteView URL pattern
                    data: {
                        'employee_ids': selectedEmployees,
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function () {
                        location.reload();
                    }
                });
            }
        } else {
            alert("Please select at least one employee to delete.");
        }
    });
});
