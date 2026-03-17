CREATE EXTERNAL TABLE IF NOT EXISTS `project-ed1531e4-86b8-41af-aef.bronze_dataset.departments` 
OPTIONS (
  format = 'JSON',
  uris = ['gs://avd-healthcare-bucket/landing/hospital/departments/*.json']
);

CREATE EXTERNAL TABLE IF NOT EXISTS `project-ed1531e4-86b8-41af-aef.bronze_dataset.encounters` 
OPTIONS (
  format = 'JSON',
  uris = ['gs://avd-healthcare-bucket/landing/hospital/encounters/*.json']
);

CREATE EXTERNAL TABLE IF NOT EXISTS `project-ed1531e4-86b8-41af-aef.bronze_dataset.patients` 
OPTIONS (
  format = 'JSON',
  uris = ['gs://avd-healthcare-bucket/landing/hospital/patients/*.json']
);

CREATE EXTERNAL TABLE IF NOT EXISTS `project-ed1531e4-86b8-41af-aef.bronze_dataset.providers` 
OPTIONS (
  format = 'JSON',
  uris = ['gs://avd-healthcare-bucket/landing/hospital/providers/*.json']
);

CREATE EXTERNAL TABLE IF NOT EXISTS `project-ed1531e4-86b8-41af-aef.bronze_dataset.transactions` 
OPTIONS (
  format = 'JSON',
  uris = ['gs://avd-healthcare-bucket/landing/hospital/transactions/*.json']
);