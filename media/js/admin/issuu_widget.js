$(document).ready(function() {
    $.getJSON('/admin/works/json_issuu_documents/', function(data) {
        var $input = $('#id_issuu_document_id');
        var input_name = $input.attr('name');
        var input_value = $input.val();
        $input.remove();
        $select = $('<select/>', {'name': input_name, 'value': input_value});
        $.each(data.rsp._content.result._content, function() {
            var $option = $('<option>', {'value': this.document.documentId});
            $option.text(this.document.title);
            if (this.document.documentId == input_value) $option.attr('selected','selected');
            $select.append($option);
        });
        $('.form-row.issuu_document_id div').append($select);
    });
});