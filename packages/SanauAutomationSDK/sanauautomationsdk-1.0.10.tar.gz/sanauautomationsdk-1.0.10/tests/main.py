# from src.SanauAutomationSDK.Worker import Worker
# from src.SanauAutomationSDK.classes.DatabaseCredentials import DatabaseCredentials
# from src.SanauAutomationSDK.classes.ArmApiCredentials import ArmApiCredentials
# from src.SanauAutomationSDK.classes.OneSApiCredentials import OneSApiCredentials
# from src.SanauAutomationSDK.database.DB import DB
# # from src.SanauAutomationSDK.database.DB import db
# from src.SanauAutomationSDK.database.models.Job import Job
#
#
# db_creds = DatabaseCredentials(name='one_s', user='pbo_client', password='0efedb9xz', host='94.247.128.101', port='5432')
# arm_api_creds = ArmApiCredentials(country='KZ', domain='pbo.kz', access_key='7nuLUYDYeQLyd3Rn')
# ones_api_creds = OneSApiCredentials(login='Проверки', password='E123456k')
#
# db = DB('one_s', user='pbo_client', password='0efedb9xz', host='94.247.128.101', port='5432').db
# job_model = Job(db=db)
# job_class = job_model.__class__
#
# worker = Worker(job_class=job_class, arm_api_credentials=arm_api_creds)
# worker.run()


from src.SanauAutomationSDK.api.arm.handlers.AlertsHandler import AlertsHandler
from src.SanauAutomationSDK.api.Wrapper import Wrapper

api_wrapper = Wrapper('KZ', 'demo.sanau.kz', 'BsUfItDXY5M79L4')
alerts_handler = AlertsHandler(api_wrapper)
# alerts_handler.create_alert(entity_id=35, key='TEEEST', message='TESTTTTT')
# alerts_handler.resolve_alert(entity_id=35, key='TEEEST')
alerts_handler.create_alert(entity_id=35, key='TEEESTTTT', message='NEW MESSAGE MESSAGE', severity=500)

# pbo_wrapper = Wrapper('KZ', 'pbo.kz', '7nuLUYDYeQLyd3Rn')
# print(pbo_wrapper.get_database(name='bagat'))
