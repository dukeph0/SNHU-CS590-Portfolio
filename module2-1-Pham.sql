--
-- PostgreSQL database dump
--

\restrict hFwfkKElzdaRyokLofxhoFubR92CncqhblWP36TBSet3TuDW7WjtWcbUlkSy9ww

-- Dumped from database version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: nutdes; Type: TABLE; Schema: public; Owner: dukeph0
--

CREATE TABLE public.nutdes (
    "Nutrient code" integer NOT NULL,
    "Nutrient description" character varying(50) NOT NULL,
    "Nutrient description abbrev" character varying(50) NOT NULL,
    "Nutrient unit" character varying(50) NOT NULL,
    "Date added" date,
    "Last modified" date
);


ALTER TABLE public.nutdes OWNER TO dukeph0;

--
-- Data for Name: nutdes; Type: TABLE DATA; Schema: public; Owner: dukeph0
--

COPY public.nutdes ("Nutrient code", "Nutrient description", "Nutrient description abbrev", "Nutrient unit", "Date added", "Last modified") FROM stdin;
203	Protein	Pro	g	1997-10-29	1997-10-29
204	Total Fat	Fat	g	1997-10-29	1997-10-29
205	Carbohydrate	Carb	g	1997-10-29	1997-10-29
207	Ash	Ash	g	1997-10-29	1997-10-29
208	Food Energy	FE	kcal	1997-10-29	1997-10-29
255	Moisture	Mois	g	1997-10-29	1997-10-29
269	Total Sugars	Sug	g	2013-12-17	2013-12-17
291	Total Dietary Fiber	TDF	g	1997-10-29	1997-10-29
301	Calcium	Ca	mg	1997-10-29	1997-10-29
303	Iron	Fe	mg	1997-10-29	1997-10-29
306	Potassium	K	mg	2017-05-02	2017-05-02
307	Sodium	Na	mg	1997-10-29	1997-10-29
320	Vitamin A, RAE	VitA, RAE	mcg	2024-10-24	2024-10-24
328	Vitamin D (D2 + D3)	VitD	mcg	2017-05-02	2017-05-02
401	Vitamin C	VitC	mg	1997-10-29	1997-10-29
539	Added Sugars	SugA	g	2022-04-01	2022-04-01
601	Cholesterol	Chol	mg	1997-10-29	1997-10-29
605	Total Trans	Trans	g	2005-11-24	2005-11-24
606	Saturated Fat	Sfat	g	1997-10-29	1997-10-29
\.


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT ALL ON SCHEMA public TO dukeph0;


--
-- PostgreSQL database dump complete
--

\unrestrict hFwfkKElzdaRyokLofxhoFubR92CncqhblWP36TBSet3TuDW7WjtWcbUlkSy9ww

