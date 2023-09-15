document.addEventListener('DOMContentLoaded', function() {
    var statusCheckbox = document.querySelector('#id_status');
    var featuredCheckbox = document.querySelector('#id_featured_products');
    var isNewCollectionCheckbox = document.querySelector('#id_is_new_collection');
    var valueInput = document.querySelector('#id_value');
    var discountInput = document.querySelector('#id_discount');
    var priceElement = document.querySelector('#id_price');

    function updateFields() {
        var value = parseFloat(valueInput.value) || 0;
        var discount = parseFloat(discountInput.value) || 0;
        var calculatedPrice = value - (value * (discount / 100));

        priceElement.value = calculatedPrice.toFixed(2);
        priceElement.disabled = true;

        if (!statusCheckbox.checked) {
            featuredCheckbox.checked = false;
            featuredCheckbox.disabled = true;
            isNewCollectionCheckbox.checked = false;
            isNewCollectionCheckbox.disabled = true;
        } else {
            featuredCheckbox.disabled = false;
            isNewCollectionCheckbox.disabled = false;
        }
    }

    function initialize() {
        updateFields();
        
        statusCheckbox.addEventListener('change', updateFields);
        valueInput.addEventListener('input', updateFields);
        discountInput.addEventListener('input', updateFields);
    }

    initialize();
});

$(document).ready(function() {
    $('#id_category').change(function() {
        var category_id = $(this).val();
        console.log("🚀 ~ category_id:", category_id)
        $.ajax({
            url: '/get_subcategories',
            data: {
                'category_id': category_id
            },
            dataType: 'json',
            success: function(data) {
                var subcategoriesSelect = $('#id_subcategory')
                subcategoriesSelect.empty();
                $.each(data.subcategories, function(index, subcategory) {
                    subcategoriesSelect.append($('<option>', {
                        value: subcategory.id,
                        text: subcategory.name
                    }));
                });
            }
        });
    });
});
