
-- requete R0

--set autotrace trace explain
set autotrace off

set sqlbl on
set timing off
set linesize 100

define D = '01-01-1998'

select count(*) 
from lineitem 
where l_shipdate <= to_date( '&D', 'DD-MM-YYYY');

select count(*) as order_count 
from orders 
where o_orderdate <= to_date( '&D', 'DD-MM-YYYY');




select count(*) as nbr_article
from lineitem;
where l_shipdate <= to_date( '&D', 'DD-MM-YYYY');


select o_orderstatus
from orders
where o_orderdate <= to_date( '&D', 'DD-MM-YYYY');



select
	l_returnflag,
	l_linestatus,
	sum(l_quantity) as sum_qty,
	sum(l_extendedprice) as sum_base_price,
	sum(l_extendedprice*(1-l_discount)) as sum_disc_price,
	sum(l_extendedprice*(1-l_discount)*(1+l_tax)) as sum_charge,
	avg(l_quantity) as avg_qty,
	avg(l_extendedprice) as avg_price,
	avg(l_discount) as avg_disc,
	count(*) as count_order	
from 
     lineitem
where 
      l_shipdate <= to_date( '&D', 'DD-MM-YYYY')
group by 
      l_linestatus,
      l_returnflag;
order by
      l_linestatus
      l_returnflag,
      



/*correction*/
select
	l_returnflag,
	l_linestatus,
	sum(l_quantity) as sum_qty,
	sum(l_extendedprice) as sum_base_price,
	sum(l_extendedprice*(1-l_discount)) as sum_disc_price,
	sum(l_extendedprice*(1-l_discount)*(1+l_tax)) as sum_charge,
	avg(l_quantity) as avg_qty,
	avg(l_extendedprice) as avg_price,
	avg(l_discount) as avg_disc,
	count(*) as count_order
from
	lineitem
where
	l_shipdate <= to_date( '&D', 'DD-MM-YYYY')
group by
      l_returnflag,
      l_linestatus
order by
      l_returnflag,
      l_linestatus;
