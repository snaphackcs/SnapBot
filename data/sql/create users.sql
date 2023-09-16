
create table
  `login_record` (
    `id` integer not null primary key autoincrement,
    `login_time` datetime not null default CURRENT_TIMESTAMP,
    `user_id` INTEGER not null,
    `comment` varchar(255) null
  )