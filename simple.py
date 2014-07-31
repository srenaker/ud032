
def parse_file(datafile):
    data = []
    counter = 0
    with open(datafile, "rb") as f:
        for line in f:
			fields = line.split(',')
			if counter == 0:
				headerline_fields = fields
			elif counter <= 10:
				d = {}
				for i in range(0, len(headerline_fields)):
					d[headerline_fields[i].strip()] = fields[i].strip()
				data.append(d)
				print d
			counter += 1	
    return data


def test():
    # a simple test of your implemetation
    datafile = "beatles-diskography.csv"
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    assert d[0] == firstline
    assert d[9] == tenthline


test()