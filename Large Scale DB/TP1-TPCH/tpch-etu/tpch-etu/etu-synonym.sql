

 
drop  synonym region;
drop  synonym nation;
drop  synonym part;
drop  synonym supplier;
drop  synonym partsupp;
drop  synonym customer;
drop  synonym orders;
drop  synonym lineitem;



-- SMALL DATABASE

create synonym region for tpch.region;
create synonym nation for tpch.nation;
create synonym part for tpch.spart;
create synonym supplier for tpch.ssupplier;
create synonym partsupp for tpch.spartsupp;
create synonym customer for tpch.scustomer;
create synonym orders for tpch.sorders;
create synonym lineitem for tpch.slineitem;



-- FULL DATABASE

--create synonym region for tpch.region;
--create synonym nation for tpch.nation;
--create synonym part for tpch.part;
--create synonym supplier for tpch.supplier;
--create synonym partsupp for tpch.partsupp;
--create synonym customer for tpch.customer;
--create synonym orders for tpch.orders;
--create synonym lineitem for tpch.lineitem;

