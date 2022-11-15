import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GgDrive():
    def __init__(self):
        self.MIN_CORRECT = 0.8
        current = os.path.dirname(os.path.realpath(__file__))
        ss_cred_path = current+'/proud-guide-366707-c99dec644bc7.json' # Your path to the json credential file
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] # define the scope
        creds = ServiceAccountCredentials.from_json_keyfile_name(ss_cred_path, scope) # add credentials to the account
        gc = gspread.authorize(creds) # authorize the clientsheet 
        spreadsheet_id = "1_4ktcz03aWYxeQRM_tpcVOJ3KmgmXqg9ybJEVF0i4Uw"
        wks = gc.open_by_key(spreadsheet_id)
        self.worksheet = wks.sheet1
        self.df = pd.DataFrame(self.worksheet.get_all_records())
    def addQuestion(self,questions: list, answers:list):
        dc = pd.DataFrame({'Questions': questions, 'Answer':answers})
        df = pd.concat([df,dc])
        self.worksheet.update([dc.columns.values.tolist()] + dc.values.tolist())
        return True
    def get(self):
        return self.df

if __name__ == "__main__":
    gg= GgDrive()
    print(gg.get())