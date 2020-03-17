$( document ).ready(function() {
    $("#createpost").click(
		function(){
			sendAjaxForm('result_form', 'ajax_form', 'createpost/');
			return false;
		}
	);
});

function sendAjaxForm(result_form, ajax_form, url) {
    $.ajax({
        url:     url, //url страницы (action_ajax_form.php)
        type:     "POST", //метод отправки
        dataType: "html", //формат данных
        data: $("#"+ajax_form).serialize(),  // Сеарилизуем объект
        success: function(response) { //Данные отправлены успешно
        	swal({
				title: "Ура!",
				text: "Данные добавлены",
				type: "success",
				confirmButtonText: "Закрыть"
			});
        	$('#ajax_form').find('input[type=text], textarea').val('');
    	},
    	error: function(response) { // Данные не отправлены
            swal({
				title: "Что-то пошло не так!",
				text: "Данные не добавлены",
				type: "error",
				confirmButtonText: "Закрыть"
			});
    	}
 	});
}


