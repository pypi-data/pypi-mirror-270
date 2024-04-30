from l10n_ar_api.afip_webservices.wsfe import wsfe
from l10n_ar_api.afip_webservices.wsaa import tokens

token_bo = """PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8c3NvIHZlcnNpb249IjIuMCI+CiAgICA8aWQgc3JjPSJDTj13c2FhLCBPPUFGSVAsIEM9QVIsIFNFUklBTE5VTUJFUj1DVUlUIDMzNjkzNDUwMjM5IiBkc3Q9IkNOPXdzZmUsIE89QUZJUCwgQz1BUiIgdW5pcXVlX2lkPSI1NDIzNzk3NjgiIGdlbl90aW1lPSIxNjUzNjM4NDI3IiBleHBfdGltZT0iMTY1MzY4MTY4NyIvPgogICAgPG9wZXJhdGlvbiB0eXBlPSJsb2dpbiIgdmFsdWU9ImdyYW50ZWQiPgogICAgICAgIDxsb2dpbiBlbnRpdHk9IjMzNjkzNDUwMjM5IiBzZXJ2aWNlPSJ3c2ZlIiB1aWQ9IlNFUklBTE5VTUJFUj1DVUlUIDMwNzE1OTIwMzQwLCBDTj1ibHVlb3JhbmdlIiBhdXRobWV0aG9kPSJjbXMiIHJlZ21ldGhvZD0iMjIiPgogICAgICAgICAgICA8cmVsYXRpb25zPgogICAgICAgICAgICAgICAgPHJlbGF0aW9uIGtleT0iMzA3MTU5MjAzNDAiIHJlbHR5cGU9IjQiLz4KICAgICAgICAgICAgPC9yZWxhdGlvbnM+CiAgICAgICAgPC9sb2dpbj4KICAgIDwvb3BlcmF0aW9uPgo8L3Nzbz4K"""
sign_bo = """LZPKVHElBSIUJtNIA+4wgabjxEtndtQim+QDmCoCBoB2UfxqFhFxnmxlf+aQaxLLoCcnogh+IhiSjPfv0vfN8BZxGy4KtghOO+YBzDYYHI6zXtSSSaxfxwehnQo2rIJ5JLMbrUEn0DRg+kqlunpiCGjtdzNFSrEvqStNIcntiX4="""
cuit = 30715920340
token = tokens.AccessToken()
token.token = token_bo
token.sign = sign_bo
token.source = """cn=wsaa,o=afip,c=ar,serialNumber=CUIT 30715920340"""
token.destination = """cn=srv1,ou=facturacion,o=empresa s.a.,c=ar,serialNumber=CUIT 30715920340"""
"""        <source>cn=wsaa,o=afip,c=ar,serialNumber=CUIT 33693450239</source>
        <destination>cn=srv1,ou=facturacion,o=empresa s.a.,c=ar,serialNumber=CUIT 30123456789</destination>
        <uniqueId>383953094</uniqueId>
        <generationTime>20011231T12:00:0203:00</generationTime>
        <expirationTime>20020101T00:00:0203:00</expirationTime>"""

wese = wsfe.Wsfe(token, cuit, homologation=False)


issued = wese.get_issued_documents()
print(issued)