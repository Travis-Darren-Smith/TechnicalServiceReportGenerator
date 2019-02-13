TechnicalServiceReportGenerator
takes data via monthly generated client technical service reports
Creates timesheet containing information on device statuses if status reports below company standards (88%)

an example of what these reports look like can be found in EXAMPLECOMPANY_Reporting Group_Technical Summary Report.pd 
However, a significant amount of information is missing due to the need to exclude client information
  
In its current version, this program has reduced the time spent on Monthly Technical Service Reports by over 50%

*Issues with .pdf to .txt conversion have resulted in the need to physically copy and paste the .pdf into the .txt file named Place_report_here.txt.
  In the future, I plan on resolving this issue by having the initial report generated in a format other than .pdf
  I also plan to incorporate the API from our company's monitoring service along with the API for our internal ticketing service 
    in order to provide feedback on failed device statuses via a fully automated system.
