from pandas import *
from streamlit import *

Data={ 'Task':['Extract','Transform','Load'],
      'Status':['Completed','Inprocess','Pending']


}
df=DataFrame(Data)

write('Etl pipeline execution ',df)
