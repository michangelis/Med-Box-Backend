insert into medb_users
values (1, 'John', 'Smith', 'jsmith@gmail.com', '6982590371', 'M', 'Forgets to take pills sometimes', '2002-08-14', './users/user1.jpg');

insert into medb_users
values (2, 'Jane', 'Doe', 'jdoe@gmail.com', '6989871356', 'F', 'Takes her pills but needs to be reminded sometimes', '1998-04-24', './users/user2.jpg');

insert into medb_users
values (3, 'David', 'Johnson', 'djohnson@gmail.com', '6943433677', 'M', 'Never takes his pills and needs to be reminded constantly', '1990-10-11', './users/user3.jpg');

insert into medb_pills
values (1, 'Acetaminophen', 'A pain reliever and fever reducer used to treat minor aches and pains, headaches, and reduce fever', 'This pill should not be taken if you are pregnant. Overdosing on acetaminophen can cause liver damage, and it should not be taken with alcohol.', 'Various', 14, './pills/Acetaminophen.jpeg', '500mg', true);

insert into medb_pills
values (2, 'Ibuprofen', 'A nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain, reduce fever, and decrease inflammation.', 'This medication can increase your risk of heart attack, stroke, and stomach bleeding, especially if taken for a long period or in high doses. Use only as directed.', 'Various', 14, './pills/Ibuprofen.jpeg', '200mg', true);

insert into medb_pills
values (3, 'Aspirin', 'A NSAID used to relieve mild to moderate pain, reduce fever, and prevent blood clots.', 'Do not give this medication to children or teenagers with a fever, as it can cause a rare but serious illness called Reye''s syndrome. Also, be aware that long-term use of aspirin can increase the risk of stomach bleeding and other side effects.', 'Various', 14, './pills/Aspirin.webp', '81mg', true);

insert into medb_pills
values (4, 'Diphenhydramine', 'A antihistamine used to relieve symptoms of allergies, such as runny nose, sneezing, and itching, as well as to treat insomnia and motion sickness.', 'This medication can cause drowsiness and impair your ability to drive or operate machinery. Avoid alcohol and other medications that can cause drowsiness when taking this medication.', 'Various', 14, './pills/Diphenhydramine.jpeg', '25mg', false);

insert into medb_pills
values (5, 'Loperamide', 'An antidiarrheal medication used to treat diarrhea and to reduce the amount of stool in people with ileostomies.', 'Do not use this medication if you have bloody or black stools, or if you have a fever. These symptoms may indicate a serious condition that requires medical attention.', 'Various', 14, './pills/Loperamide.webp', '2mg', false);

insert into medb_pills
values (6, 'Famotidine', 'A histamine-2 blocker used to treat and prevent heartburn and acid indigestion caused by gastroesophageal reflux disease (GERD).', 'TDo not take this medication if you are allergic to famotidine or other acid reducers. Also, tell your doctor if you have kidney disease or if you are taking other medications that can interact with famotidine.', 'Various', 14, './pills/Famotidine.webp', '20mg', false);


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

select *
from medb_pills;

select medb_users.first_name, medb_pills.name
from medb_users, medb_user_prescription_pill, medb_pills
where medb_users.id = medb_user_prescription_pill.user_id and medb_user_prescription_pill.per_pill_id=medb_pills.id

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
values (12, 1, '/Users/Desktop/Alarm.wav', '15:00:00', 5, 6);

insert into medb_alarm
values (12, 1, '/Users/Desktop/Alarm.wav', '23:00:00', 5, 6);

delete from medb_alarm where id=12;

select *
from medb_comment;

insert into medb_comment
values (1, 'This pill was fantastic', 1, 1);


insert into medb_comment
values (2, 'This pill was awful', 1, 2);

insert into medb_comment
values (3, 'This pill was ok', 1, 3);

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
values (9, false, 12, '2023-04-14');/*David*/


select medb_users.first_name, count(medb_users.first_name)
from medb_taken, medb_alarm, medb_user_prescription_pill, medb_users
where medb_taken.taken=false and medb_alarm.id = medb_taken.alarm_id and medb_alarm.user_prescription_pill_id = medb_user_prescription_pill.id and medb_user_prescription_pill.user_id = medb_users.id
group by medb_users.first_name;


select medb_alarm.id, medb_users.first_name, medb_alarm.time, medb_days.day
from medb_alarm, medb_user_prescription_pill, medb_users, medb_days
where medb_alarm.user_prescription_pill_id = medb_user_prescription_pill.id and medb_user_prescription_pill.user_id = medb_users.id and medb_alarm.day_id = medb_days.id;

select medb_users.first_name, medb_comment.commentText, medb_pills.name
from medb_comment, medb_users, medb_pills
where medb_pills.id = 1 and medb_comment.pill_id = medb_pills.id and medb_comment.user_id = medb_users.id;

select medb_users.first_name, medb_users.last_name
from medb_alarm, medb_days, medb_users, medb_user_prescription_pill
where medb_days.day = 'Monday' and medb_days.id = medb_alarm.id and medb_alarm.user_prescription_pill_id = medb_user_prescription_pill.id and medb_user_prescription_pill.user_id = medb_users.id;

select medb_users.first_name, medb_pills.name, medb_alarm.time
from medb_users, medb_user_prescription_pill, medb_alarm, medb_days, medb_pills
where medb_days.day = 'Wednesday' and medb_days.id = medb_alarm.day_id and medb_alarm.user_prescription_pill_id = medb_user_prescription_pill.id and medb_users.id = medb_user_prescription_pill.user_id and medb_user_prescription_pill.per_pill_id = medb_pills.id;


