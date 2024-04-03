$(document).on('click', '#addUnit', function(event){
    event.preventDefault();
    nam = $('#nam').val();
    locid = $('#locid').val();
    comdid = $('#comdid').val();
    if (nam && locid != '0' && comdid != '0'){
        form = $('#unitForm')[0]
        req = $.ajax({
            url:'/clerk/add-unit',
            type:'post',
            contentType: false,
            processData: false,
            data: new FormData(form)
        });
        req.done(function(res){
            if (res.error){
                alert(res.error);
            }else{
                alert('Unit Added Successfully');
                form.reset();
            }
        });
    }else{
        alert('Please enter required fields')
    }
});