SELECT a.year, 
a.average as `CO hr - A`, 
b.average as `PM2,5 - BAM hr - A`, 
c.average as `O3 hr - A`, 
d.average as `NOx hr - A`,
-- other 4 months
e.average as `CO hr - B`, 
f.average as `PM2,5 - BAM hr - B`, 
g.average as `O3 hr - B`, 
h.average as `NOx hr - B`

from 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM data 
where Label = 'CO hr' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) a
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM data 
where Label = 'PM2,5 - BAM hr' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) b 
on a.year = b.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM data 
where Label = 'O3 hr' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) c 
on a.year = c.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM data 
where Label = 'NOx hr' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) d
on a.year = d.year

-- other months

left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM data 
where Label = 'CO hr' 
and month(timestamp) in (1,2,3,4,9,10,11,12)
group by year(timestamp)
) e
on a.year = e.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM data 
where Label = 'PM2,5 - BAM hr' 
and month(timestamp) in (1,2,3,4,9,10,11,12)
group by year(timestamp)
) f
on a.year = f.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM data 
where Label = 'O3 hr' 
and month(timestamp) in (1,2,3,4,9,10,11,12)
group by year(timestamp)
) g
on a.year = g.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM data 
where Label = 'NOx hr' 
and month(timestamp) in (1,2,3,4,9,10,11,12)
) h
on a.year = h.year