create table users
(
    id   int,
    name varchar(100)
);

create table movies
(
    id    int,
    title varchar(100)
);

create table movie_ratings
(
    movie_id   int,
    user_id    int,
    rating     int,
    created_at date
);

drop table movies;

insert into movies value (1, 'Aver');
insert into movies value (2, 'Alad');
insert into movies value (3, 'Aqua');
insert into users value (1, 'Ben');
insert into users value (2, 'Nicole');
insert into users value (3, 'James');
insert into users value (4, 'Tara');
select *
from movies;

insert into movie_ratings value (1, 1, 3, '2019-05-07 00:10:00');
insert into movie_ratings value (1, 2, 4, '2019-04-07 00:10:00');
insert into movie_ratings value (1, 3, 5, '2019-05-11 00:10:00');
insert into movie_ratings value (1, 4, 4, '2019-05-02 00:10:00');
insert into movie_ratings value (2, 1, 4, '2019-06-07 00:10:00');
insert into movie_ratings value (2, 2, 3, '2019-05-30 00:10:00');
insert into movie_ratings value (2, 3, 4, '2019-06-07 00:10:00');
insert into movie_ratings value (3, 1, 5, '2019-01-07 00:10:00');
insert into movie_ratings value (3, 2, 4, '2019-01-07 00:10:00');

select title
from movies a,
     (select movie_id, avg(rating) as avg
      from (
               select *
               from movie_ratings
               where created_at like '2019-05%'
           ) c
      group by movie_id
      order by avg desc
      limit 1
          offset 1) b
where a.id = b.movie_id;

select title
from movies a,
     (select movie_id, avg(rating) as avg
      from (
               select *
               from movie_ratings
               where created_at like '2019-05%'
           ) c
      group by movie_id
      order by avg desc
      limit 1
          offset 1) b
where a.id = b.movie_id;


select movie_id, avg(rating) as avg
from (
         select *
         from movie_ratings
         where created_at like '2019-05%'
     ) c
group by movie_id
order by avg desc
limit 1
    offset 1;


create table table1
(
    districtid varchar(100),
    region     varchar(100)
);
create table table2
(
    partnerid   varchar(100),
    partnertype varchar(100),
    districtid  varchar(100)

);

insert into table1
values ('SD001', 'East');
insert into table1
values ('SD002', 'West');
insert into table1
values ('SD003', 'North');
insert into table1
values ('SD004', 'South');
insert into table1
values ('SD005', 'East');
insert into table1
values ('SD006', 'North');

insert into table2
values ('P1001', 'Bus', 'SD002');
insert into table2
values ('P1002', 'Civic', 'SD003');
insert into table2
values ('P1003', 'Bus', 'SD004');
insert into table2
values ('P1004', 'Gov', 'SD005');
insert into table2
values ('P1005', 'Gov', 'SD003');

select *
from table1;
select *
from table2;

select a.region,
       b.PartnerType,
       count(PartnerID) as Total
from table1 a
         right join table2 b
                    on
                        a.districtid = b.districtid
group by a.region;


select u.name
from movie_ratings
         right join users u on user_id = u.id
group by user_id
order by count(user_id) desc
limit 1;


select title
from movies a,
     (select movie_id, avg(rating) as avg
      from (
               select *
               from movie_ratings
               where created_at like '2019-05%'
           ) c
      group by movie_id
      order by avg desc
      limit 1) b
where a.id = b.movie_id;


select a.title
from (
         select title, avg(rating) as avg
         from movie_ratings
                  left join movies m on movie_ratings.movie_id = m.id and created_at like '2019-05%'
         group by movie_id
         order by avg desc
         limit 1
     ) as a;

select title
from movie_ratings
         right join movies m on movie_ratings.movie_id = m.id and created_at like '2019-05%'
group by movie_id
order by avg(rating) desc;


create table table4 as (
    select a.region,
           b.PartnerType,
           count(PartnerID) as Total
    from table1 a
             right join table2 b
                        on
                            a.districtid = b.districtid
    group by a.region, b.PartnerType
);
select *
from table4;