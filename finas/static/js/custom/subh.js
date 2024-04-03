$(document).on('click', '#addSubh', function(event){
    event.preventDefault();
    form = $('#subhForm')[0]
    req = $.ajax({
        url:'/clerk/add-subh',
        type:'post',
        contentType: false,
        processData: false,
        data: new FormData(form)
    });
    req.done(function(res){
        if (res.error){
            alert(res.error);
        }else{
            alert('Sub Head Code Registered Successfully');
            form.reset();
        }
    });
});