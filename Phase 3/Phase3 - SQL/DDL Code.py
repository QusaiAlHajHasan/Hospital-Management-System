*****************************************************************************************************************************************************
CREATE TABLE bill (
  bill_number INTEGER CONSTRAINT pk_bill PRIMARY KEY,
  patient_type VARCHAR(10) NOT NULL,
  health_card INTEGER,
  number_of_day INTEGER,
  room_charge INTEGER,
  doctor_charge INTEGER,
  nurse_charge INTEGER,
  medicine_charge INTEGER
);
*****************************************************************************************************************************************************
CREATE TABLE department (
  department_name VARCHAR(10) CONSTRAINT pk_department PRIMARY KEY,
  department_phone INTEGER NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE department_head (
  dept_head_id INTEGER CONSTRAINT pk_department_head PRIMARY KEY,
  dept_head_name VARCHAR(5) NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE active_employee (
  employee_id INTEGER CONSTRAINT pk_active_employee PRIMARY KEY,
  employee_name VARCHAR(5) NOT NULL,
  employee_gender VARCHAR(6) NOT NULL,
  employee_dob DATE NOT NULL,
  salary INTEGER,
  hire_date DATE,
  certain_time DATETIME NOT NULL,
  dept_head_id INTEGER NOT NULL
);
*****************************************************************************************************************************************************
ALTER TABLE active_employee ADD CONSTRAINT fk_active_employee__department_head FOREIGN KEY (dept_head_id) REFERENCES department_head (dept_head_id);
*****************************************************************************************************************************************************
CREATE TABLE doctor (
  employee_id INTEGER CONSTRAINT pk_active_employee PRIMARY KEY,
  employee_name VARCHAR(5) NOT NULL,
  employee_gender VARCHAR(6) NOT NULL,
  employee_dob DATE NOT NULL,
  salary INTEGER,
  hire_date DATE,
  qualification VARCHAR(10) NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE emergency_contact (
  emergency_contact_id INTEGER CONSTRAINT pk_emergency_contact PRIMARY KEY,
  emergency_contact_name VARCHAR(10) NOT NULL,
  relation_with_patient VARCHAR(10) NOT NULL,
  emergency_contact_phone INTEGER NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE medicine (
  code INTEGER CONSTRAINT pk_medicine PRIMARY KEY,
  dosage VARCHAR(10) NOT NULL,
  price INTEGER NOT NULL,
  quantity VARCHAR(10) NOT NULL,
  description VARCHAR(11) NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE nurse (
  employee_id INTEGER CONSTRAINT pk_active_employee PRIMARY KEY,
  employee_name VARCHAR(5) NOT NULL,
  employee_gender VARCHAR(6) NOT NULL,
  employee_dob DATE NOT NULL,
  salary INTEGER5,
  hire_date DATE,
  ward_number INTEGER NOT NULL,
  services_provided VARCHAR(18) NOT NULL,
);
*****************************************************************************************************************************************************
CREATE TABLE passive_employee (
  employee_id INTEGER CONSTRAINT pk_active_employee PRIMARY KEY,
  employee_name VARCHAR(5) NOT NULL,
  employee_gender VARCHAR(6) NOT NULL,
  employee_dob DATE NOT NULL,
  salary INTEGER,
  hire_date DATE,
  leave_date DATE NOT NULL,
  corresponding_department VARCHAR(10) NOT NULL,
  department_name VARCHAR(10) NOT NULL,
);
*****************************************************************************************************************************************************
ALTER TABLE passive_employee ADD CONSTRAINT fk_passive_employee__department FOREIGN KEY (department_name) REFERENCES department (department_name);
*****************************************************************************************************************************************************
CREATE TABLE reception (
  telephone_number INTEGER CONSTRAINT pk_reception PRIMARY KEY,
  employees_name VARCHAR(5) NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE out_patient (
  patient_id INTEGER CONSTRAINT pk_out_patient PRIMARY KEY,
  patient_name VARCHAR(5) NOT NULL,
  phone_number INTEGER,
  patient_gender VARCHAR(6) NOT NULL,
  patient_dob DATE,
  discharging_date DATE NOT NULL,
  recieving_date DATE NOT NULL,
  disease VARCHAR(11) NOT NULL,
  status VARCHAR(5) NOT NULL,
  blood_group VARCHAR(5) NOT NULL,
  address VARCHAR(5) NOT NULL,
  e_mail VARCHAR(7) NOT NULL,
  ambulatory_services VARCHAR(10),
  bill_number INTEGER NOT NULL,
  telephone_number INTEGER NOT NULL
);
*****************************************************************************************************************************************************
ALTER TABLE out_patient ADD CONSTRAINT fk_out_patient__bill FOREIGN KEY (bill_number) REFERENCES bill (bill_number);
*****************************************************************************************************************************************************
ALTER TABLE out_patient ADD CONSTRAINT fk_out_patient__reception FOREIGN KEY (telephone_number) REFERENCES reception (telephone_number);
*****************************************************************************************************************************************************
CREATE TABLE doctor_out_patients (
  employee_id INTEGER NOT NULL,
  patient_id INTEGER NOT NULL,
  CONSTRAINT pk_doctor_out_patients PRIMARY KEY (patient_id, employee_id)
);
*****************************************************************************************************************************************************
ALTER TABLE doctor_out_patients ADD CONSTRAINT fk_doctor_out_patients__doctor FOREIGN KEY (employee_id) REFERENCES doctor (employee_id);
*****************************************************************************************************************************************************
ALTER TABLE doctor_out_patients ADD CONSTRAINT fk_doctor_out_patients__out_patient FOREIGN KEY (patient_id) REFERENCES out_patient (patient_id);
*****************************************************************************************************************************************************
CREATE TABLE medicine_out_patients (
  patient_id INTEGER NOT NULL,
  code INTEGER NOT NULL,
  CONSTRAINT pk_medicine_out_patients PRIMARY KEY (patient_id, code)
);
*****************************************************************************************************************************************************
ALTER TABLE medicine_out_patients ADD CONSTRAINT fk_medicine_out_patients__medicine FOREIGN KEY (code) REFERENCES medicine (code);
*****************************************************************************************************************************************************
ALTER TABLE medicine_out_patients ADD CONSTRAINT fk_medicine_out_patients__out_patient FOREIGN KEY (patient_id) REFERENCES out_patient (patient_id);
*****************************************************************************************************************************************************
CREATE TABLE nurse_out_patients (
  employee_id INTEGER NOT NULL,
  patient_id INTEGER NOT NULL,
  CONSTRAINT pk_nurse_out_patients PRIMARY KEY (patient_id, employee_id)
);
*****************************************************************************************************************************************************
ALTER TABLE nurse_out_patients ADD CONSTRAINT fk_nurse_out_patients__nurse FOREIGN KEY (employee_id) REFERENCES nurse (employee_id);
*****************************************************************************************************************************************************
ALTER TABLE nurse_out_patients ADD CONSTRAINT fk_nurse_out_patients__out_patient FOREIGN KEY (patient_id) REFERENCES out_patient (patient_id);
*****************************************************************************************************************************************************
CREATE TABLE receptionest (
  employee_id INTEGER CONSTRAINT pk_active_employee PRIMARY KEY,
  employee_name VARCHAR(5) NOT NULL,
  employee_gender VARCHAR(6) NOT NULL,
  employee_dob DATE NOT NULL,
  salary INTEGER,
  hire_date DATE,
  professionalism VARCHAR(10),
  effictive_communication VARCHAR(10),
  interpersonal_aplomb VARCHAR(10),
  multitasking_capabilities VARCHAR(10),
  organizational_abilities VARCHAR(10),
  technical_prowess VARCHAR(10)
);
*****************************************************************************************************************************************************
CREATE TABLE record (
  record_number INTEGER CONSTRAINT pk_record PRIMARY KEY,
  appointment DATE NOT NULL,
  employee_id INTEGER NOT NULL
);
*****************************************************************************************************************************************************
ALTER TABLE record ADD CONSTRAINT fk_record__receptionest FOREIGN KEY (employee_id) REFERENCES receptionest (employee_id);
*****************************************************************************************************************************************************
CREATE TABLE room (
  room_id INTEGER CONSTRAINT pk_room PRIMARY KEY,
  room_cost INTEGER NOT NULL,
  extension VARCHAR(3),
  status VARCHAR(5) NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE in_patient (
  patient_id INTEGER CONSTRAINT pk_inpatient PRIMARY KEY,
  patient_name VARCHAR(5) NOT NULL,
  phone_number INTEGER,
  patient_gender VARCHAR(6) NOT NULL,
  patient_dob DATE,
  discharging_date DATE NOT NULL,
  recieving_date DATE NOT NULL,
  disease VARCHAR(11) NOT NULL,
  status VARCHAR(5) NOT NULL,
  blood_group VARCHAR(5) NOT NULL,
  address VARCHAR(5) NOT NULL,
  e_mail VARCHAR(7) NOT NULL,
  last_day DATE NOT NULL, 
  room_no INTEGER,
  room_id INTEGER NOT NULL,
  bill_number INTEGER NOT NULL,
  telephone_number INTEGER NOT NULL
);
*****************************************************************************************************************************************************
ALTER TABLE in_patient ADD CONSTRAINT fk_in_patient__bill FOREIGN KEY (bill_number) REFERENCES bill (bill_number);
*****************************************************************************************************************************************************
ALTER TABLE in_patient ADD CONSTRAINT fk_in_patient__reception FOREIGN KEY (telephone_number) REFERENCES reception (telephone_number);
*****************************************************************************************************************************************************
ALTER TABLE in_patient ADD CONSTRAINT fk_in_patient__room FOREIGN KEY (room_id) REFERENCES room (room_id);
*****************************************************************************************************************************************************
CREATE TABLE doctor_in_patients (
  employee_id INTEGER NOT NULL,
  patient_id INTEGER NOT NULL,
  CONSTRAINT pk_doctor_in_patients PRIMARY KEY (patient_id, employee_id)
);
*****************************************************************************************************************************************************
ALTER TABLE doctor_in_patients ADD CONSTRAINT fk_doctor_in_patients__doctor FOREIGN KEY (employee_id) REFERENCES doctor (employee_id);
*****************************************************************************************************************************************************
ALTER TABLE doctor_in_patients ADD CONSTRAINT fk_doctor_in_patients__inpatient FOREIGN KEY (patient_id) REFERENCES in_patient (patient_id);
*****************************************************************************************************************************************************
CREATE TABLE emergency_contact_in_patients (
  patient_id INTEGER NOT NULL,
  emergency_contact_id INTEGER NOT NULL,
  CONSTRAINT pk_emergencycontact_in_patients PRIMARY KEY (patient_id, emergency_contact_id)
);
*****************************************************************************************************************************************************
ALTER TABLE emergency_contact_in_patients ADD CONSTRAINT fk_emergency_contact_in_patients__emergency_contact FOREIGN KEY (emergency_contact_id) REFERENCES emergency_contact (emergency_contact_id);
*****************************************************************************************************************************************************
ALTER TABLE emergencycontact_in_patients ADD CONSTRAINT fk_emergency_contact_in_patients__in_patient FOREIGN KEY (patient_id) REFERENCES in_patient (patient_id);
*****************************************************************************************************************************************************
CREATE TABLE in_patient_medicines (
  patient_id INTEGER NOT NULL,
  code INTEGER NOT NULL,
  CONSTRAINT pk_in_patient_medicines PRIMARY KEY (patient_id, code)
);
*****************************************************************************************************************************************************
ALTER TABLE in_patient_medicines ADD CONSTRAINT fk_in_patient_medicines__inpatient FOREIGN KEY (patient_id) REFERENCES in_patient (patient_id);
*****************************************************************************************************************************************************
ALTER TABLE in_patient_medicines ADD CONSTRAINT fk_in_patient_medicines__medicine FOREIGN KEY (code) REFERENCES medicine (code);
*****************************************************************************************************************************************************
CREATE TABLE in_patient_nurses (
  employee_id INTEGER NOT NULL,
  patient_id INTEGER NOT NULL,
  CONSTRAINT pk_inpatient_nurses PRIMARY KEY (patient_id, employee_id)
);
*****************************************************************************************************************************************************
ALTER TABLE in_patient_nurses ADD CONSTRAINT fk_in_patient_nurses__in_patient FOREIGN KEY (patient_id) REFERENCES in_patient (patient_id);
*****************************************************************************************************************************************************
ALTER TABLE in_patient_nurses ADD CONSTRAINT fk_in_patient_nurses__nurse FOREIGN KEY (employee_id) REFERENCES nurse (employee_id);
*****************************************************************************************************************************************************
CREATE TABLE nurse_rooms (
  employee_id INTEGER NOT NULL,
  room_id INTEGER NOT NULL,
  CONSTRAINT pk_nurse_rooms PRIMARY KEY (room_id, employee_id)
);
*****************************************************************************************************************************************************
ALTER TABLE nurse_rooms ADD CONSTRAINT fk_nurse_rooms__nurse FOREIGN KEY (employee_id) REFERENCES nurse (employee_id);
*****************************************************************************************************************************************************
ALTER TABLE nurse_rooms ADD CONSTRAINT fk_nurse_rooms__room FOREIGN KEY (room_id) REFERENCES room (room_id);
*****************************************************************************************************************************************************
CREATE TABLE service (
  emergency_department VARCHAR(35) CONSTRAINT pk_service PRIMARY KEY,
  observation VARCHAR(10) NOT NULL,
  surgery VARCHAR(18) NOT NULL,
  lab_tests VARCHAR(20) NOT NULL,
  x_ray VARCHAR(10) NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE out_patient_services (
  patient_id INTEGER NOT NULL,
  emergency_department VARCHAR(35) NOT NULL,
  CONSTRAINT pk_out_patient_services PRIMARY KEY (patient_id,emergency_department)
);
*****************************************************************************************************************************************************
ALTER TABLE out_patient_services ADD CONSTRAINT fk_out_patient_services__out_patient FOREIGN KEY (patient_id) REFERENCES out_patient (patient_id);
*****************************************************************************************************************************************************
ALTER TABLE out_patient_services ADD CONSTRAINT fk_out_patient_services__service FOREIGN KEY (emergency_department) REFERENCES service (emergency_department);
*****************************************************************************************************************************************************
CREATE TABLE test (
  test_type VARCHAR(10) NOT NULL,
  test_name VARCHAR(20) CONSTRAINT pk_test PRIMARY KEY,
  test_cost INTEGER NOT NULL
);
*****************************************************************************************************************************************************
CREATE TABLE doctor_tests (
  employee_id INTEGER NOT NULL,
  test_type VARCHAR(10) NOT NULL,
  CONSTRAINT pk_doctor_tests PRIMARY KEY (test_type, employee_id)
);
*****************************************************************************************************************************************************
ALTER TABLE doctor_tests ADD CONSTRAINT fk_doctor_tests__doctor FOREIGN KEY (employee_id) REFERENCES doctor (employee_id);
*****************************************************************************************************************************************************
ALTER TABLE doctor_tests ADD CONSTRAINT fk_doctor_tests__test FOREIGN KEY (test_name) REFERENCES test (test_name);
*****************************************************************************************************************************************************
CREATE TABLE in_patient_tests (
  patient_id INTEGER NOT NULL,
  test_name VARCHAR(10) NOT NULL,
  CONSTRAINT pk_in_patient_tests PRIMARY KEY (patient_id, test_name)
);
*****************************************************************************************************************************************************
ALTER TABLE in_patient_tests ADD CONSTRAINT fk_in_patient_tests__inpatient FOREIGN KEY (patient_id) REFERENCES in_patient (patient_id);
*****************************************************************************************************************************************************
ALTER TABLE in_patient_tests ADD CONSTRAINT fk_in_patient_tests__test FOREIGN KEY (test_name) REFERENCES test (test_name);
*****************************************************************************************************************************************************
CREATE TABLE out_patient_tests (
  patient_id INTEGER NOT NULL,
  test_name VARCHAR(10) NOT NULL,
  CONSTRAINT pk_out_patient_tests PRIMARY KEY (patient_id,test_name)
);
*****************************************************************************************************************************************************
ALTER TABLE out_patient_tests ADD CONSTRAINT fk_out_patient_tests__out_patient FOREIGN KEY (patient_id) REFERENCES out_patient (patient_id);
*****************************************************************************************************************************************************
ALTER TABLE out_patient_tests ADD CONSTRAINT fk_out_patient_tests__test FOREIGN KEY (test_name) REFERENCES test (test_name)
*****************************************************************************************************************************************************
CREATE TABLE contact_NO (
  contact_number INTEGER NOT NULL;
  employee_id INTEGER NOT NULL'
  CONSTRAINT pk_contact_NO PRIMARY KEY (contact_number,employee_id)
  );
  ***************************************************************************************************************************************************
  CREATE TABLE roomType (
  room_type VARCHAR(14) NOT NULL;
  room_id INTEGER NOT NULL'
  CONSTRAINT pk_roomType PRIMARY KEY (room_type,room_id)
  );
  ***************************************************************************************************************************************************
  CREATE TABLE patientInfo (
  patient_info VARCHAR(20) NOT NULL;
  record_number INTEGER NOT NULL'
  CONSTRAINT pk_contact_NO PRIMARY KEY (patient_info,record_number)
  );
  ***************************************************************************************************************************************************