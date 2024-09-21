$('#getValues').on('click', function() {
    var selectedValues = $('#select').val(); // Получаем выбранные значения
    $('#output').text('Выбранные значения: ' + selectedValues.join(', ')); // Выводим их
  });