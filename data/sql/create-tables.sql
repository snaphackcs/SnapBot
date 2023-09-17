
create table
  `users` (
    `id` integer not null primary key autoincrement,
    `created_at` timestamp not null default CURRENT_TIMESTAMP,
    `wechat_id` INTEGER not null,
    `username` varchar(255) not null,
    `pinyin` varchar(255) not null,
    `admin` integer not null default 0,
    `status` integer default 1
  );

create table
  `log_user` (
    `id` integer not null primary key autoincrement,
    `created_at` timestamp not null default CURRENT_TIMESTAMP,
    `user_id` integer not null,
    `operation` varchar(255)
  );

create table
  `title` (
    `user_id` integer not null,
    `title` varchar(10),
    `status` integer default 1
  );

create table 
  `sign` (
    `id` integer not null primary key autoincrement,
    `user_id` integer not null,
    `sign_date` timestamp not null default CURRENT_TIMESTAMP,
    `sign_day` integer not null default 0,
    `compulitity` compulitity not null default 0,
    `comment` varchar(255) null
  );

create table
  `student` (
    `id` integer not null primary key autoincrement,
    `user_id` integer not null,
    `year` integer not null,
    `grade` integer not null,
    `class` integer not null,
    `status` integer default 1
  );

create table
  `register` (
    `student_id` integer not null,
    `lesson_id` integer not null,
    `status` integer not null default 1
  );

create table
  `lesson` (
    `id` integer not null primary key autoincrement,
    `year` integer not null,
    `grade` integer not null,
    `lesson_type` varchar(25) not null,
    `lesson_name` varchar(25) not null,
    `status` integer not null default 1
  );

create table
  `lesson_table` (
    `id` integer not null primary key autoincrement,
    `year` integer not null,
    `grade` integer not null,
    `class` integer not null,
    `table` varchar(255) not null,
    `status` integer not null default 1
  );