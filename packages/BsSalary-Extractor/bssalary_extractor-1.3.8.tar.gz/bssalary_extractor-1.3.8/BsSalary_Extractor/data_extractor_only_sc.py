from BsSalary_Extractor.functions import *
import BsSalary_Extractor.constants as const
from unidecode import unidecode
import re
import numpy as np
import openai
from google.cloud import vision_v1
import os
import json
from google.oauth2.service_account import Credentials
import arabic_reshaper
import PyPDF2
import ast
from io import BytesIO

class BsSalary_Extractor:
        
        def __init__(self, pdf_bytes, customer_name, api_key, credentials_str=None, customer_name_ar=None):
                
                self.pdf_bytes = pdf_bytes
                self.customer_name = customer_name
                self.customer_name_ar = customer_name_ar
                self.api_key = api_key
                credentials_dict = json.loads(credentials_str)
                credentials = Credentials.from_service_account_info(credentials_dict)
                self.client = vision_v1.ImageAnnotatorClient(credentials=credentials)
                self.salary_keywords_arabic = [
                                        "أجر", "اجر", "الأجر", "الاجر",
                                        "معاش", "المعاش",
                                        "دخل",  "الدخل",
                                        "أرباح", "ارباح", "الأرباح", "الارباح",
                                        "كسب",  "الكسب",
                                        "استحقاق",  "الاستحقاق",
                                        "إيراد", "ايراد", "الإيراد", "الايراد",
                                        "المكافاة","الراتب","راتب", 'مكافأة','المكافأة','مكافاة',
                                    ]

                
                self.reshaped_salary_keywords_arabic = [arabic_reshaper.reshape(arabic_str) for arabic_str in self.salary_keywords_arabic]
                
        def get_sal_and_name_from_SC(self, data):
            openai.api_key = self.api_key
            data = limit_string_to_tokens(data, 20000)
            
            prompt = f"I am sharing you a data of Salary Certificate, I need you to extract the name, company name, designation, date_of_issue from it wherever you find it and I also need you to extract the salary wherever you find it, the salary can be find using keywords such as 'salary' or 'total salary' or 'net salary' or 'gross monthly salary' or 'wage'. In case where you are confused with extracting the salary, or you cannot find the total or gross salary, please find basic pay, housing allowance, transportation allowance, other allowances, etc.. and sum all of them to get the 'salary'. Note that if you are still not able to find salary due to multiple numbers coming in, then take the number that comes along with the currency like AED, SAR, etc.. and get the highest number among all and assign it as the salary. Make sure that designation is extracted correctly, as it can also be in as 'job function' or 'occupation', etc.. Note that designation can be confusing as it may match with designation of the person who issued the salary certificate, but your logic should be only to get the designation of the person for whom the salary certificate is made, if you're not able to find designation then just give it as None or an empty string. Note: Also make sure to extract the currency from the data, if currency is in some other language then translate it to english and only output it in standard format like USD, AED, SAR, etc.. here's the data please do the job, make sure that your response should be in a dictionary format having the respective key and value pairs. If you find issue_date confusing due to multiple dates coming in then take the date that is greatest among all as the issue_date, In cases of date in Hijri date format then convert it to Gregorian Date format. Remember to output the issue_date in dd/mm/yyyy format only. If you're not able to find the currency directly then identify the currency by the address or location or country written in the data. return only the fields required, nothing apart from it: {data}"
            
            user_message = [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-16k",
                    messages=user_message,
                    temperature=0.2,
                    max_tokens=3500
                )
            return response.choices[0]["message"]["content"]
        
        def handle_salary_fields_extraction(self, extraction_input):
                extraction_input = eastern_arabic_to_english(extraction_input)
                extraction_input = extraction_input.replace("،", ",")

                result_data = self.get_sal_and_name_from_SC(str(extraction_input))
                
                print(f"\n\nGPT RESULT: {result_data}\n\n")

                try:
                    result_data = result_data.lower()
                    result_data = ast.literal_eval(result_data)
                except:
                    try: 
                        result_data = result_data.lower()
                        json_string = json.dumps(result_data)
                        json_data_bytes = json_string.encode('utf-8')
                        result_data = json.loads(json_data_bytes)
                        print(f"result: {result_data}")
                    except:
                        return {'error': 'extraction_unsuccessfull', 'salary': 0, 'name': '', 'company_name': '', 'designation': '', 'currency': '', 'date_of_issue': ''} 

                try:
                    result_data['extracted_data'] = extraction_input
                except:
                    return {'error': 'extraction_unsuccessfull', 'salary': 0, 'name': '', 'company_name': '', 'designation': '', 'currency': '', 'date_of_issue': ''} 

                if result_data.get('name', '').lower() == 'john doe' or result_data.get('company_name', '').lower() in ['abc company', 'xyz company'] or result_data.get('designation').lower() == 'software engineer':
                    
                    doc = fitz.open(stream=self.pdf_bytes, filetype="pdf")
                    data = get_scanned_pdf_text(self.client, doc)
                    result_data = self.get_sal_and_name_from_SC(str(data))

                    # print(f"\n\nGPT RESULT 2: {result_data}\n\n")

                    try:
                        result_data = result_data.lower()
                        result_data = ast.literal_eval(result_data)
                    except:
                        return {'error': 'extraction_unsuccessfull', 'salary': 0, 'name': '', 'company_name': '', 'designation': '', 'currency': '', 'date_of_issue': ''}

                    result_data['extracted_data'] = data
                
                if result_data.get('date_of_issue', '') and not re.match(r'^\d{2}/\d{2}/\d{4}$', result_data.get('date_of_issue', '')):
                    result_data['date_of_issue'] = clean_and_convert_date(result_data['date_of_issue'])

                if re.match(r'^\d{2}/\d{2}/\d{4}$', result_data.get('date_of_issue', '')):
                    result_data['date_of_issue'] = hijri_to_gregorian(result_data['date_of_issue'])

                result_data['salary'] = clean_salary(result_data.get('salary', ''))
                result_data['salary'] = eastern_arabic_to_english(result_data.get('salary', ''))

                ## handle salary decimal in start
                l = [i for i in result_data['salary']]
                if len(l)>0 and l[0] == '.':
                        result_data['salary'] = ''.join(result_data['salary'][1:])
                
                Name_check = validate_name_both(self.customer_name.lower(), self.customer_name_ar.lower(), result_data.get('name', '').lower())
                # if not Name_check:
                    # return {'error': 'name_mismatch_error', 'name': '', 'company_name': '', 'designation': '', 'date_of_issue': '', 'salary': '', 'currency': ''}
                
                is_more_than_3_months = months_difference_with_grace_period(result_data.get('date_of_issue', ''))>=3
                # if is_more_than_3_months:
                    # return {'error': 'overdated_salary_certificate', 'name': '', 'company_name': '', 'designation': '', 'date_of_issue': '', 'salary': '', 'currency': ''}

                if result_data.get('name', '').lower() == 'john doe':
                    result_data['name'] = ''

                if result_data.get('company_name', '').lower() in ['abc company', 'xyz company']:
                    result_data['company_name'] = ''

                if result_data.get('designation', '').lower() == 'software engineer':
                    result_data['designation'] = ''

                return result_data
        
        
        def extract_data_for_sc(self):
            extraction_input = perform_data_extraction(self.client, self.pdf_bytes)
            data = self.handle_salary_fields_extraction(extraction_input)

            try:
                salary_length = len(str(int(convert_sal_string_to_number(data['salary']))))
                if salary_length>=6:
                    data['salary'] = ''
            except:
                pass

            return data

        def standardize_keys(self, data):
            key_mapping = {
                'name': 'name',
                'Name': 'name',
                'Customer Name': 'name',
                'Employee Name': 'name',
                'company_name': 'company_name',
                'Company Name': 'company_name',
                'designation': 'designation',
                'Designation': 'designation',
                'currency': 'currency',
                'Currency': 'currency',
                'date_of_issue': 'date_of_issue',
                'Date of Issue': 'date_of_issue',
                'salary': 'salary',
                'Salary': 'salary'
            }

            standardized_data = {}

            try:
                for key, value in data.items():
                    if key in key_mapping:
                        standardized_data[key_mapping[key]] = value
                    else:
                        standardized_data[key] = value

                return standardized_data
            
            except:
                return data

        def extract_data(self):
            ### 1. Data Extraction (from pdf) -------------------
            try:
                doc = fitz.open(stream=self.pdf_bytes, filetype="pdf")
                page_count=doc.page_count
                print(f"PAGE COUNT: {page_count}")
            except:
                raise Exception("Unrecognized or Unsupported Document")
            
            if page_count>2:
                raise Exception("Not Salary Certificate")
                # return {'error': 'not_salary_certificate', 'error_details': 'more than 2 pages'}

            extraction_input = perform_data_extraction(self.client, self.pdf_bytes, only_first_page=True)
            translated_extraction = translate_ar_to_en(extraction_input)

            if not contains_salary(arabic_reshaper.reshape(extraction_input.replace("\n", "")), self.reshaped_salary_keywords_arabic) and 'salary' not in extraction_input.lower() and 'salary' not in translated_extraction.lower():
                raise Exception("Not Salary Certificate")
                # return {'error': 'not_salary_certificate', 'error_details': 'no keywords found', 'extracted_data': extraction_input}
            
            else:
                print("SALARY FLOW")
                # try:

                result = self.extract_data_for_sc()
                print("result generated here")
                result = self.standardize_keys(result)

                ## handle case where SC is overdated so we raise an exception to re upload
                if result.get('error', '') and result.get('error', '') == 'overdated_salary_certificate':
                    raise Exception("Overdated Salary Certificate")
                
                ## handle failure case to make 2nd call to gpt so that we get data this time
                elif result.get('error', '') and result.get('error', '') == 'extraction_unsuccessfull':
                    result_data = self.extract_data_for_sc()
                    print("result generated here 2")
                    result_data = self.standardize_keys(result_data)
                    return result_data
                
                else:
                    return result
            
                # except Exception as e:
                #         reader = PyPDF2.PdfReader(self.pdf_bytes)
                #         # Extract text from first page
                #         text = ''
                #         page = reader.pages[0]
                #         text = page.extract_text()
                        
                #         if not text:
                #             raise Exception("Unrecognized or Unsupported Document")
                        
                #         result_data = self.handle_salary_fields_extraction(text)
                #         print("result generated here 2")
                #         result_data = self.standardize_keys(result_data)
                #         return result_data
                    
                        # return {'error': 'extraction_unsuccessfull', 'salary': 0, 'name': '', 'company_name': '', 'designation': '', 'currency': '', 'date_of_issue': ''} 
            
