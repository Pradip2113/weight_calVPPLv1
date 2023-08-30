# Copyright (c) 2023, Abhishek Chougule and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
class CaneWeight(Document):
	#-----------------------------------------------------------------------------------------------------------------
	@frappe.whitelist()
	def get_bridge_info(self):
		# self.user_name=frappe.db.get_value("User", frappe.session.user, "full_name")
		doc = frappe.db.get_list("WB Master Setting",filters={"operator_name": frappe.session.user } ,fields=["name","operator_name","weight_bridge_no"])
		if doc:
			self.operator_name= doc[0].name
			self.wb= doc[0].weight_bridge_no
		else:
			frappe.throw("User do not have any permission to access any weight bridge")
		wbstatus=frappe.get_doc("Weight Reading", "weight-reading")
		temp=wbstatus.wb1_status
		rolenm=frappe.db.get_value("User", frappe.session.user, "role_profile_name")
		if str(rolenm)=="WB User":
			if temp=="Connected.":
				if self.wb=="Weight Bridge 1":
					temp=wbstatus.wb1_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
				if self.wb=="Weight Bridge 2":
					temp=wbstatus.wb2_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
				if self.wb=="Weight Bridge 3":
					temp=wbstatus.wb3_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
				if self.wb=="Weight Bridge 4":
					temp=wbstatus.wb4_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
				if self.wb=="Weight Bridge 5":
					temp=wbstatus.wb5_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
			else:   
				if self.wb=="Weight Bridge 1":
					temp=wbstatus.wb1_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
				if self.wb=="Weight Bridge 2":
					temp=wbstatus.wb2_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
				if self.wb=="Weight Bridge 3":
					temp=wbstatus.wb3_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
				if self.wb=="Weight Bridge 4":
					temp=wbstatus.wb4_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
				if self.wb=="Weight Bridge 5":
					temp=wbstatus.wb5_status
					frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")

	# @frappe.whitelist()
	# def get_qty(self):
	# 	# cfactor=0
	# 	for u in self.get('items'):
	# 		if u.uom=="KG":
	# 			u.qty=self.actual_weight
	# 		if u.uom=="TON":
	# 			u.qty=self.actual_weight*0.001

			#     batch=frappe.db.get_list("Item")
			#     for b in batch:
			#         eachbatch = frappe.get_doc("Item", b.name)
			#         for i in eachbatch.get('uoms'):
			#             for m in self.items:
			#                 if m.item_code==b.name:
			#                     if i.uom=="KG":
			#                         cfactor=i.conversion_factor
			#     u.qty=self.actual_weight*cfactor
			# else:
			#     u.qty=1.00







	@frappe.whitelist()
	def get_loaded_weight(self):
		doc=frappe.get_doc("Weight Reading")
		if self.wb=="Weight Bridge 1":
			self.loaded_weight=doc.wm1
		if self.wb=="Weight Bridge 2":
			self.loaded_weight=doc.wm2
		if self.wb=="Weight Bridge 3":
			self.loaded_weight=doc.wm3
		if self.wb=="Weight Bridge 4":
			self.loaded_weight=doc.wm4
		if self.wb=="Weight Bridge 5":
			self.loaded_weight=doc.wm5

	@frappe.whitelist()
	def get_empty_weight(self):
		# if is_internet_available:
		#     frappe.msgprint('Internet Available')
		doc=frappe.get_doc("Weight Reading")
		if self.wb=="Weight Bridge 1":
			self.empty_weight=doc.wm1
		if self.wb=="Weight Bridge 2":
			self.empty_weight=doc.wm2
		if self.wb=="Weight Bridge 3":
			self.empty_weight=doc.wm3
		if self.wb=="Weight Bridge 4":
			self.empty_weight=doc.wm4
		if self.wb=="Weight Bridge 5":
			self.empty_weight=doc.wm5


	# @frappe.whitelist()
	# def is_internet_available():
	#   try:
	#       requests.get('https://www.google.com')
	#       return True
	#   except requests.ConnectionError:
	#       return False


	@frappe.whitelist()
	def get_actual_weight(self):
		self.actual_weight=self.loaded_weight-self.empty_weight
		self.set_binding_weight()
		self.actual_weight= (self.loaded_weight-self.empty_weight)-((self.binding_weight)/1000)
		self.set_weight_id_water_supplier()
	@frappe.whitelist()
	def before_save(self):
		self.validate_net_weight()
  
	@frappe.whitelist()
	def before_submit(self):
		self.set_value_at_cane_weight_no()
		self.update_counter_at_branch()
  
	@frappe.whitelist()
	def before_cancel(self):
		self.on_cancel_update_counter_at_branch()
  
	@frappe.whitelist()
	def validate_net_weight(self):
		if self.actual_weight < 0:
			frappe.throw('Weight can not be negative')
   
	@frappe.whitelist()
	def set_value_at_cane_weight_no(self):
		current_value= frappe.get_value("Branch",self.branch,"cane_weight_no")
		if not self.cane_weight_no:
			self.cane_weight_no = current_value+1
			# frappe.throw(str(self.cane_weight_no))

   
	@frappe.whitelist()
	def update_counter_at_branch(self):
		if self.cane_weight_no:
			frappe.set_value("Branch",self.branch,"cane_weight_no",self.cane_weight_no)

	@frappe.whitelist()
	def on_cancel_update_counter_at_branch(self):
		current_value= frappe.get_value("Branch",self.branch,"cane_weight_no")
     
		if self.cane_weight_no==current_value:
			frappe.set_value("Branch",self.branch,"cane_weight_no",(self.cane_weight_no-1))
 
	@frappe.whitelist()
	def set_binding_weight(self):
		value_per_weight = frappe.get_value("Branch",self.branch,"binding_weight_per_ton")
		if value_per_weight:
			self.binding_weight = self.actual_weight*value_per_weight
   
		else:
			frappe.throw(f'Set Binding Weight Quentity per Ton In Branch "{self.branch}"')
   
	@frappe.whitelist()
	def set_weight_id_water_supplier(self):
		if self.water_supplier_code:
			a_w=float(self.actual_weight)
			w_p=float(self.water_share)
			water_supplier_weight = ((a_w * w_p)/100)
			change_actual_weight = (a_w- water_supplier_weight)
			self.actual_weight=change_actual_weight
			self.water_supplier_weight = water_supplier_weight
	
    #To get the shift type
	@frappe.whitelist()
	def get_shift(self):
		current_time = datetime.datetime.now().time()
		child_table = frappe.get_all("Child Shift Setting", filters={
			"parent": self.branch,
		}, fields=["shift", "start_time", "end_time"])
		for shift_setting in child_table:
			start_time = shift_setting.start_time.total_seconds()
			end_time = shift_setting.end_time.total_seconds()
			current_seconds = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
			if start_time <= current_seconds <= end_time:
				self.shft = shift_setting.shift
				break

	# @frappe.whitelist()
	# def append_qty(self):
	#   for i in self.items:
	#       if str(i.item_group)=='Sugar':
	#           i.qty=self.actual_weight

	#-----------------------------------------------------------------------------------------------------------------
