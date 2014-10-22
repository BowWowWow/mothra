
BEGIN;
use mothra;
TRUNCATE TABLE `reports_dealerdailyhitlist`;
TRUNCATE TABLE `reports_dealermarketreport`;
TRUNCATE TABLE `reports_userprofile`;
TRUNCATE TABLE `reports_marketreportyearmonth`;
TRUNCATE TABLE `reports_dealersite`;
TRUNCATE TABLE `reports_dealer`;
TRUNCATE TABLE `reports_dealergroup`;
TRUNCATE TABLE `reports_dataiumdma`;

COMMIT;
