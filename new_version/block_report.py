def block_report (conn, cursor, file_number, table):
	import block_report_data
	block_report_info (conn, cursor, file_number, table)
	tumour_biopsy_data(conn, cursor, file_number, table)
	lymphnode_biopsy(conn, cursor, file_number, table)
	surgery_info (conn, cursor, file_number, table)