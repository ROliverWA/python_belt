$(document).ready(function(){
    $('#reg_email').keyup(function(){
        // alert('bam');
        $.ajax({url: '/check_email',
        method: 'POST',
        data: $('#reg_email').serialize(),
        success: function(result){
            $('#ajax_email').text('Email is already registered.')            
                 },
        error: function(result){
            $('#ajax_email').text('Email is not registered.')
        }
        })})


    })
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
