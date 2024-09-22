import requests

access_code = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlhrUFpfSmhoXzlTYzNZS01oRERBZFBWeFowOF9SUzI1NiIsInBpLmF0bSI6ImFzc2MifQ.eyJzY29wZSI6WyJkYXRhOnJlYWQiXSwiY2xpZW50X2lkIjoiTzFqMlU1MWNUYkx2dUxUUlVPZHFIWVVLRlJEWk5TMzJjaHRzUFhSRTlxd0dqQW9jIiwiaXNzIjoiaHR0cHM6Ly9kZXZlbG9wZXIuYXBpLmF1dG9kZXNrLmNvbSIsImF1ZCI6Imh0dHBzOi8vYXV0b2Rlc2suY29tIiwianRpIjoieGVkelZJQTFIY21sb1hTekRWd3JWMWdYZ0o5SmhmUXJNWmVrUU56ektLUzNRYnNKZUlyNlV4RFVuQTBBaFdNNiIsImV4cCI6MTcyNjk4NTYxMiwidXNlcmlkIjoiUUhaMkZCTEdQV0FaVTRWNyJ9.OkDOAXxywCmB5er2wV8NgYKY5pTUYy2l8_OhPS2tnwCvvSU9kM_YHQM3TqtD7WklIdblV3W3LUiyRB8BN8pgnLinaSPZZquzB3PfQ-UfkELWcRPqbE3sexTYdZNblVENA7visZSVcSX2cGMH_DY4p_oNK9olm21j8fvFkll5VOUUPqrDSy4I83WvS0fD3Wc6OdsEh7IUQF6We8VBK3VDgEiUOhFNW_QXoRTwKhiIX8imgt3sS0ZdEtaOVYCfEV8cm1VJSzuNPGXewxgfJ5gofZC_CWTB-w_7pM7sN6b5zbzFNsINhUljUUV3g9MvUIiJCxJK7iPHzNwRqFMu-mBn0A"
project_id = "pro_2wet97vhty"

def get_proposals(access_code):
    url = f"https://developer.api.autodesk.com/forma/proposal/v1alpha/proposals?authcontext={project_id}&limit=100"
    payload = {}
    headers = {
    'Authorization': f'Bearer {access_code}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def get_elements(proposals, access_code):
    master_list = []
    for proposal in proposals["results"]:
        for building_index in range(len(proposal["children"])):
            if building_index != 0:
                continue
            else:
                building_urn = proposal["children"][building_index]["urn"]
                # print(building_urn)
                url = f"https://developer.api.autodesk.com/forma/element-service/v1alpha/elements/{building_urn}?authcontext={project_id}"

                payload = {}
                headers = {
                'Authorization': f'Bearer {access_code}'
                }
                response = requests.request("GET", url, headers=headers, data=payload)
                master_list.append(response.json())
    
    return master_list
                





proposals = get_proposals(access_code)
buildings = get_elements(proposals, access_code)

print(buildings)
