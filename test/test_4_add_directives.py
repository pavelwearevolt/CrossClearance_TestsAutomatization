__author__ = 'pavelkosicin'


def test_add_directives(app):
    # songwriter_number - the songwriter's serial number in which the directive is created
    app.song.open_add_directives_modal_window(songwriter_number="2")
    app.song.fill_territory_field(
        territory_field_id="license_origin_select_search",
        territory="world",
        territory_locator="tt-suggestion.suggestion-0"
    )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="1"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="2"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="3"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="5"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="4"
        )
    app.song.fill_percentage_field(
        percentage_field_id="payment-percentage-input",
        percentage="50"
        )
    app.song.save_button()
