--
-- PostgreSQL database dump
--

\restrict TX25ee4aJyP6ksB98Hp1k2ZzaGdAZYzBUGhy6mytv2KHuLQIkxYEZCAg8PjFhBY

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
-- Name: nutdes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nutdes (
    "Nutrient code" integer NOT NULL,
    "Nutrient description" character varying(200),
    "Nutrient symbol" character varying(50),
    "Unit of measure" character varying(20),
    "Creation date" date,
    "Update date" date
);


ALTER TABLE public.nutdes OWNER TO postgres;

--
-- Data for Name: nutdes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.nutdes ("Nutrient code", "Nutrient description", "Nutrient symbol", "Unit of measure", "Creation date", "Update date") FROM stdin;
\.


--
-- Name: nutdes nutdes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nutdes
    ADD CONSTRAINT nutdes_pkey PRIMARY KEY ("Nutrient code");


--
-- PostgreSQL database dump complete
--

\unrestrict TX25ee4aJyP6ksB98Hp1k2ZzaGdAZYzBUGhy6mytv2KHuLQIkxYEZCAg8PjFhBY

