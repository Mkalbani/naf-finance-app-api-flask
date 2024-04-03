$(document).on('click', '#newTrans', function(event){
    console.log('is working')
    event.preventDefault();
    form = $('#newTransForm')[0]
    req = $.ajax({
        url:'/clerk/new-trans',
        type:'post',
        contentType: false,
        processData: false,
        data: new FormData(form)
    });
    req.done(function(res){
        if (res.error){
            alert(res.error);
        }else{
            alert('Transaction Committed Successfully');
            form.reset();
        }
    });
});