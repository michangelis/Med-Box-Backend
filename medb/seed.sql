-- USERS
insert into medb_users
values (1, 'John', 'Smith', 'jsmith@gmail.com', '6982590371', 'M', 'Forgets to take pills sometimes', '2002-08-14', './users/user1.jpg', 'password');

insert into medb_users
values (2, 'Jane', 'Doe', 'jdoe@gmail.com', '6989871356', 'F', 'Takes her pills but needs to be reminded sometimes', '1998-04-24', './users/user2.jpg', 'password');

insert into medb_users
values (3, 'David', 'Johnson', 'djohnson@gmail.com', '6943433677', 'M', 'Never takes his pills and needs to be reminded constantly', '1990-10-11', './users/user3.jpg', 'password');

-- MEDICINE PILLS
insert into medb_pills
values (1, 'Acetaminophen', 'A pain reliever and fever reducer used to treat minor aches and pains, headaches, and reduce fever', 'This pill should not be taken if you are pregnant. Overdosing on acetaminophen can cause liver damage, and it should not be taken with alcohol.', 'Various', 14, './pills/Acetaminophen.jpeg', '500mg', true, 1);

insert into medb_pills
values (2, 'Ibuprofen', 'A nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain, reduce fever, and decrease inflammation.', 'This medication can increase your risk of heart attack, stroke, and stomach bleeding, especially if taken for a long period or in high doses. Use only as directed.', 'Various', 14, './pills/Ibuprofen.jpeg', '200mg', true, 1);

insert into medb_pills
values (3, 'Aspirin', 'A NSAID used to relieve mild to moderate pain, reduce fever, and prevent blood clots.', 'Do not give this medication to children or teenagers with a fever, as it can cause a rare but serious illness called Reye''s syndrome. Also, be aware that long-term use of aspirin can increase the risk of stomach bleeding and other side effects.', 'Various', 14, './pills/Aspirin.webp', '81mg', true, 1);

insert into medb_pills
values (4, 'Diphenhydramine', 'A antihistamine used to relieve symptoms of allergies, such as runny nose, sneezing, and itching, as well as to treat insomnia and motion sickness.', 'This medication can cause drowsiness and impair your ability to drive or operate machinery. Avoid alcohol and other medications that can cause drowsiness when taking this medication.', 'Various', 14, './pills/Diphenhydramine.jpeg', '25mg', false, 1);

insert into medb_pills
values (5, 'Loperamide', 'An antidiarrheal medication used to treat diarrhea and to reduce the amount of stool in people with ileostomies.', 'Do not use this medication if you have bloody or black stools, or if you have a fever. These symptoms may indicate a serious condition that requires medical attention.', 'Various', 14, './pills/Loperamide.webp', '2mg', false, 1);

insert into medb_pills
values (6, 'Famotidine', 'A histamine-2 blocker used to treat and prevent heartburn and acid indigestion caused by gastroesophageal reflux disease (GERD).', 'TDo not take this medication if you are allergic to famotidine or other acid reducers. Also, tell your doctor if you have kidney disease or if you are taking other medications that can interact with famotidine.', 'Various', 14, './pills/Famotidine.webp', '20mg', false, 1);


-- PRESCRIPTION PILLS
insert into medb_user_prescription_pill
values (1, 1, 1);

insert into medb_user_prescription_pill
values (2, 2, 1);

insert into medb_user_prescription_pill
values (3, 1, 2);

insert into medb_user_prescription_pill
values (4, 2, 2);

insert into medb_user_prescription_pill
values (5, 2, 3);

insert into medb_user_prescription_pill
values (6, 3, 3);


--DAYS
insert into medb_days
values (1, 'Monday');
insert into medb_days
values (2, 'Tuesday');
insert into medb_days
values (3, 'Wednesday');
insert into medb_days
values (4, 'Thursday');
insert into medb_days
values (5, 'Friday');
insert into medb_days
values (6, 'Saturday');
insert into medb_days
values (7, 'Sunday');

-- ALARM SCHEDULES
insert into medb_alarm
values (1, 1, '/Users/Desktop/Alarm.wav', '10:00:00', 1, 1);

insert into medb_alarm
values (2, 2, '/Users/Desktop/Alarm.wav', '22:00:00', 1, 2);

insert into medb_alarm
values (3, 1, '/Users/Desktop/Alarm.wav', '12:00:00', 2, 3);

insert into medb_alarm
values (4, 2, '/Users/Desktop/Alarm.wav', '18:00:00', 2, 4);

insert into medb_alarm
values (5, 1, '/Users/Desktop/Alarm.wav', '10:00:00', 1, 1);

insert into medb_alarm
values (6, 2, '/Users/Desktop/Alarm.wav', '22:00:00', 1, 2);

insert into medb_alarm
values (7, 1, '/Users/Desktop/Alarm.wav', '12:00:00', 4, 3);

insert into medb_alarm
values (8, 2, '/Users/Desktop/Alarm.wav', '18:00:00', 4, 4);

insert into medb_alarm
values (9, 1, '/Users/Desktop/Alarm.wav', '19:00:00', 4, 5);

insert into medb_alarm
values (10, 2, '/Users/Desktop/Alarm.wav', '23:00:00', 4, 6);

insert into medb_alarm
values (11, 2, '/Users/Desktop/Alarm.wav', '14:00:00', 4, 6);

insert into medb_alarm
values (12, 1, '/Users/Desktop/Alarm.wav', '15:00:00', 5, 6);

insert into medb_alarm
values (13, 1, '/Users/Desktop/Alarm.wav', '13:00:00', 1, 1);

insert into medb_alarm
values (14, 1, '/Users/Desktop/Alarm.wav', '11:35:00', 1, 1);

insert into medb_alarm
values (15, 1, '/Users/Desktop/Alarm.wav', '11:37:00', 1, 3);

insert into medb_alarm
values (16, 1, '/Users/Desktop/Alarm.wav', '13:02:00', 1, 3);

insert into medb_alarm
values (17, 1, '/Users/Desktop/Alarm.wav', '14:09:00', 1, 3);

insert into medb_alarm
values (18, 1, '/Users/Desktop/Alarm.wav', '14:15:00', 1, 3);

insert into medb_alarm
values (19, 1, '/Users/Desktop/Alarm.wav', '14:17:00', 1, 3);

insert into medb_alarm
values (20, 1, '/Users/Desktop/Alarm.wav', '16:46:00', 1, 3);

insert into medb_alarm
values (21, 1, '/Users/Desktop/Alarm.wav', '16:48:00', 1, 3);

insert into medb_alarm
values (22, 1, '/Users/Desktop/Alarm.wav', '16:49:00', 1, 3);

insert into medb_alarm
values (23, 1, '/Users/Desktop/Alarm.wav', '16:52:00', 1, 3);

insert into medb_alarm
values (24, 1, '/Users/Desktop/Alarm.wav', '16:55:00', 1, 3);

insert into medb_alarm
values (25, 1, '/Users/Desktop/Alarm.wav', '17:05:00', 1, 3);

insert into medb_alarm
values (26, 1, '/Users/Desktop/Alarm.wav', '17:07:00', 1, 3);

insert into medb_alarm
values (27, 1, '/Users/Desktop/Alarm.wav', '17:09:00', 1, 3);

insert into medb_alarm
values (28, 1, '/Users/Desktop/Alarm.wav', '17:17:00', 1, 3);

insert into medb_alarm
values (29, 1, '/Users/Desktop/Alarm.wav', '10:30:00', 2, 4);

insert into medb_alarm
values (30, 1, '/Users/Desktop/Alarm.wav', '10:32:00', 2, 4);

insert into medb_alarm
values (31, 1, '/Users/Desktop/Alarm.wav', '23:03:00', 2, 4);

insert into medb_alarm
values (32, 1, '/Users/Desktop/Alarm.wav', '23:13:00', 2, 4);

insert into medb_alarm
values (33, 1, '/Users/Desktop/Alarm.wav', '23:17:00', 2, 4);

insert into medb_alarm
values (34, 1, '/Users/Desktop/Alarm.wav', '23:45:00', 2, 4);

insert into medb_alarm
values (35, 1, '/Users/Desktop/Alarm.wav', '23:47:00', 2, 4);


--COMMENTS
insert into medb_comment
values (1, 'This pill was fantastic', 1, 1);

insert into medb_comment
values (2, 'This pill was awful', 1, 2);

insert into medb_comment
values (3, 'This pill was ok', 1, 3);


--INTAKE MONITOR TAKEN PILLS
insert into medb_taken
values (1, true, 1, '2023-04-10');/*John*/

insert into medb_taken
values (2, true, 2, '2023-04-10');/*John*/

insert into medb_taken
values (3, false, 3, '2023-04-11');/*Jane*/

insert into medb_taken
values (4, true, 4, '2023-04-11');/*Jane*/

insert into medb_taken
values (5, false, 5, '2023-04-12');/*David*/

insert into medb_taken
values (6, false, 6, '2023-04-12');/*David*/

insert into medb_taken
values (7, false, 7, '2023-04-13');/*Jane*/

insert into medb_taken
values (8, false, 11, '2023-04-13');/*David*/

insert into medb_taken
values (9, false, 12, '2023-04-14');

--MOTORS
insert into medb_motor
values (1, 'motor1.py', 'dmotor1.py');

insert into medb_motor
values (2, 'motor2.py', 'dmotor2.py');

insert into medb_motor
values (3, 'motor3.py', 'dmotor3.py');

insert into medb_motor
values (4, 'motor4.py', 'dmotor4.py');


