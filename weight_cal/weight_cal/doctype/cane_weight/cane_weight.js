// Copyright (c) 2023, Abhishek Chougule and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cane Weight', {
    refresh: function(frm) {
        $('.layout-side-section').hide();
        $('.layout-main-section-wrapper').css('margin-left', '0');
    }
});

frappe.ui.form.on('Cane Weight', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Cane Weight', {
    get_loaded_weight: function(frm) {
            frappe.model.set_value("Cane Weight", frm.doc.name, 'gross_weight_timedate', frappe.datetime.get_datetime_as_string());
    }
});
frappe.ui.form.on('Cane Weight', {
    get_empty_weight: function(frm) {
            frappe.model.set_value("Cane Weight", frm.doc.name, 'tear_weight_timedate', frappe.datetime.get_datetime_as_string());
    }
});


frappe.ui.form.on('Cane Weight', {
	onload: function (frm) {
		frm.call({
			method:'get_bridge_info',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	refresh: function (frm) {
		frm.call({
			method:'get_bridge_info',
			doc: frm.doc,
		});
	}
})



frappe.ui.form.on('Cane Weight', {
	branch: function (frm) {
		frm.call({
			method:'get_shift',
			doc: frm.doc,
		});
	}
})
// frappe.ui.form.on('Cane Weight', {
// 	onload: function (frm) {
// 		frm.call({
// 			method:'get_empty_weight',
// 			doc: frm.doc,
// 		});
// 	}
// })

frappe.ui.form.on('Cane Weight', {
	get_loaded_weight: function (frm) {
		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
		frm.call({
			method:'get_loaded_weight',
			doc: frm.doc,
		});
	}
})

// frappe.ui.form.on('Cane Weight', {
// 	get_loaded_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })

// frappe.ui.form.on('Cane Weight', {
// 	loaded_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })

// frappe.ui.form.on('Cane Weight', {
// 	empty_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })


// frappe.ui.form.on('Cane Weight', {
// 	get_empty_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })

frappe.ui.form.on('Cane Weight', {
	onload: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	get_loaded_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	get_empty_weight: function (frm) {
		frm.call({
			method:'get_empty_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	get_empty_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})
// frappe.ui.form.on('Cane Weight Item', {
// 	item_code: function (frm) {
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,
// 		});
// 	}
// })

frappe.ui.form.on('Cane Weight', {
	loaded_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	empty_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})