from flet import *

import json
def main(page:Page):
	mydata = [
	{"name":"jou","male":False},
	{"name":"dwq","male":True},
	{"name":"grge","male":False},
	{"name":"tre","male":True},
	{"name":"htrtr","male":False},
	]


	tb = DataTable(
		columns=[
			DataColumn(Text("name")),
			DataColumn(Text("male")),

		],
		rows=[]

		)
	def changename(e,data,index):
		you_edit = e.control.value
		print(you_edit)
		for i,x in enumerate(mydata):
			if i == index:
				mydata[index]['name'] = you_edit
				break

		# AND PRINT NEW UPDATE DATA IN SNACKBAR
		new_data = json.dumps(mydata)
		page.snack_bar = SnackBar(
			Text(new_data,size=20),
			bgcolor="black"
			)
		page.snack_bar.open = True
		page.update()

	def updategender(e,x,index):
		gender_value = e.control.value
		print(gender_value)
		for i,x in enumerate(mydata):
			if i == index:
				mydata[index]['male'] = gender_value
				break

		# AND PRINT NEW UPDATE DATA IN SNACKBAR
		new_data = json.dumps(mydata)
		page.snack_bar = SnackBar(
			Text(new_data,size=20),
			bgcolor="black"
			)
		page.snack_bar.open = True
		page.update()


	# LOOP AND ADD TO TABLE
	for i,x in enumerate(mydata):
		tb.rows.append(
			DataRow(
				cells=[
				DataCell(
					Row([
						Dropdown(
						# PASS PARAMETER TO LAMBDA 
						# FUNCTION
					on_change=lambda e,i=i:changename(e,x,i),
					# AND REMOVE BORDER IN DROPDOWN
					border=InputBorder.NONE,
					hint_text=x['name'],
					width=100,
					options=[
					dropdown.Option(x['name']) for x in mydata
					]
							)
						])
					),
				DataCell(
					Column([
						Checkbox(value=x['male'],
					on_change=lambda e,i=i:updategender(e,x,i)
						)
						])
					)
				]
				)
			)


	page.add(
	Column([
		tb
		])
		)
flet.app(target=main)
