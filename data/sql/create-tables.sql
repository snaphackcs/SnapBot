
create table
  `users` (
    `id` integer not null primary key autoincrement,
    `created_at` timestamp not null default CURRENT_TIMESTAMP,
    `wechat_id` INTEGER not null,
    `username` varchar(255) not null,
    `pinyin` varchar(255) not null,
    `admin` integer not null,
    `status` integer default 1
  )

create table 
  `sign` (
    `id` integer not null primary key autoincrement,
    `user_id` integer not null,
    `sign_date` timestamp not null default CURRENT_TIMESTAMP,
    `sign_day` integer not null default 0,
    `compulitity` compulitity not null default 0,
    `comment` varchar(255) null
  )

create table
  `title` (
    `user_id` integer not null,
    `title` varchar(10),
    `status` integer default 1
  )

create table
  `student` (
    `id` integer not null primary key autoincrement,
    `user_id` integer not null,
    `created_at` timestamp not null default CURRENT_TIMESTAMP,
    `grade` integer not null,
    `class` integer not null,
    `status` integer default 1
  )

create table
  `register` (
    `student_id` integer not null,
    `lesson_id` integer not null,
    `status` integer not null default 1
  )

create table
  `lessons` (
    `id` integer not null primary key autoincrement,
    `grade` integer not null,
    `lesson_type` varchar(255) not null,
    `registered_lesson` varchar(255) not null,
    `status` integer not null default 1
  )