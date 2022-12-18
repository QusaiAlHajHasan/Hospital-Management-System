                                                 **********PROJECT(PI)**********
select patient_type,bill_number from bill; 
select department_name from department;
select dept_head_id from department_head;
select employee_id,salary from active_employee;
select employee_name,qualification from doctor;
select emergency_contact_id,emergency_contact_phone from emergency_contact;
select code,price from medicine;
select employee_id,ward_number from nurse;
select employee_name,leave_date from passive_employee;
select telephone_number from reception;
select patient_id,patient_name,disease from out_patient;
select patient_id,employee_id from doctor_out_patients;
select patient_id,code from medicine_out_patients;
select patient_id,employee_id from nurse_out_patients;
select employee_name,professionalism from receptionest;
select record_number,appointment from record;
select room_id,status from room;
select patient_id,recieving_date from in_patient;
select patient_id,employee_id from doctor_in_patients;
select patient_id,emergency_contact_id from emergency_contact_in_patients;
select patient_id,code from in_patient_medicines;
select patient_id,employee_id from in_patients_nurses;
select employee_id,room_id from nurse_rooms;
select emergency_department,lab_tests from service;
select patient_id,emergency_department from out_patient_services;
select test_name,test_cost from test;
select employee_id,test_type from doctor_tests;
select patient_id,test_type from in_patient_tests;
select patient_id,test_type from out_patient_tests;
select contact_number,employee_id from contact_NO;
select room_type,room_id from roomType;
select patient_info,record_number from patientInfo;
*****************************************************************************************************************************************************
                                                  **********SELECT(SIGMA)**********
select * from bill where patient_type='outpatient'; 
select * from department where department_phone=07912553;
select * from department_head where dept_head_name='Ayman';
select * from active_employee where employee_gender='Male';
select * from doctor where employee_id>=358;
select * from emergency_contact where relation_with_patient='Brother';
select * from medicine where dosage='2m';
select * from nurse where employee_gender='Female';
select * from passive_employee where salary>400;
select * from reception where employee_name='Ahmad';
select * from out_patient where address='Irbid';
select * from doctor_out_patients where patient_id<564;
select * from medicine_out_patients where code=12;
select * from nurse_out_patients where employee_id=25;
select * from receptionest where employee_gender='Male';
select * from record where record_number>102;
select * from room where room_cost>200;
select * from in_patient where status='Bad';
select * from doctor_in_patients where patient_id=17;
select * from emergency_contact_in_patients where emergency_contact_id>236;
select * from in_patient_medicines where code=11;
select * from in_patients_nurses where employee_id=24;
select * from nurse_rooms where room_id=105;
select * from service where x_ray='Skull';
select * from out_patient_services where patient_id>10;
select * from test where test_name='Fat test';
select * from doctor_tests where employee_id>500;
select * from in_patient_tests where test_name='Liver function test';
select * from out_patient_tests where patient_id<9;
select * from contact_NO where contact_number<20;
select * from roomType where room_id<500;
select * from patientInfo where record_number>70;
*****************************************************************************************************************************************************
                                                     **********RENAME(P)**********
alter table out_patient rename employee_id to emp_id;
alter table in_patient rename employee_name to emp_name;
alter table department rename department_name to dept_name;
alter table reception rename telephone_numbet to tele_no;
alter table emergency_contact rename emergency_contact_id to em_cont_id;
alter table nurse rename employee_gender to emp_gender;
*****************************************************************************************************************************************************
                                                      **********JOIN**********
select employee_name,dept_head_name from active_employee,department_head where active_employee.dept_head_id=department_head.dept_head_id;
select employee_name,department_phone from passive_employee,department where passive_employee.department_name=department.department_name; 
select patient_name,room_charge from out_patient,bill where bill.bill_number=out_patient.bill_number;
select employee_name,record_number from receptionest,record where record.employee_id=receptionest.employee_id;
select patient_name,room_cost from in_patient,room where in_patient.room_id=room.room_id ;
*****************************************************************************************************************************************************
                                                 **********CARTESIAN PRODUCT**********
select employee_name,dept_head_name from active_employee,department_head;
select employee_name,department_phone from passive_employee,department; 
select patient_name,room_charge from out_patient,bill;
select employee_name,record_number from receptionest,record;
select patient_name,room_cost from in_patient,room;
*****************************************************************************************************************************************************
                                                    **********INTERSECTION**********
select * from active_employee,department_head;
select * from passive_employee,department; 
select * from out_patient,bill;
select * from receptionest,record;
select * from in_patient,room;
*****************************************************************************************************************************************************