SELECT a.year, 
a.average as `O3 hr - A`, 
b.average as `PM2,5 - BAM hr - A`, 
c.average as `NOx hr - A`,
-- other 4 months
d.average as `O3 hr - B`, 
e.average as `PM2,5 - BAM hr - B`, 
f.average as `NOx hr - B`

from 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM qc_saint_garnier 
where Label = 'O3 hr' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) a
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM qc_saint_garnier 
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
FROM qc_saint_garnier 
where Label = 'NOx hr' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) c 
on a.year = c.year

-- other months

left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM qc_saint_garnier 
where Label = 'O3 hr' 
and month(timestamp) in (1,2,3,4,9,10,11,12)
group by year(timestamp)
) d
on a.year = d.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM qc_saint_garnier 
where Label = 'PM2,5 - BAM hr' 
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
FROM qc_saint_garnier 
where Label = 'NOx hr'
and month(timestamp) in (1,2,3,4,9,10,11,12)
) f
on a.year = f.year