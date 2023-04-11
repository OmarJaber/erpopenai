// Copyright (c) 2023, Omar Jaber and contributors
// For license information, please see license.txt

frappe.ui.form.on('OpenAi Chat', {
	send: function(frm) {
		frm.set_value("response", )
		frappe.call({
	        doc: cur_frm.doc,
	        method: "generate_text",
	        freeze: true,
	        callback: function(r) {
	        	if(r){
	            	frm.set_value("response", r.message)
	            }
	        }
	    });
	}
});
