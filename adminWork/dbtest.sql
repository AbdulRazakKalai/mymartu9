--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: adminlogin; Type: TABLE; Schema: public; Owner: martu9
--

CREATE TABLE adminlogin (
    id integer NOT NULL,
    username text NOT NULL,
    password text
);


ALTER TABLE adminlogin OWNER TO martu9;

--
-- Name: adminlogin_id_seq; Type: SEQUENCE; Schema: public; Owner: martu9
--

CREATE SEQUENCE adminlogin_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE adminlogin_id_seq OWNER TO martu9;

--
-- Name: adminlogin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: martu9
--

ALTER SEQUENCE adminlogin_id_seq OWNED BY adminlogin.id;


--
-- Name: productlist; Type: TABLE; Schema: public; Owner: martu9
--

CREATE TABLE productlist (
    id integer NOT NULL,
    product_id text NOT NULL,
    category text
);


ALTER TABLE productlist OWNER TO martu9;

--
-- Name: productlist_id_seq; Type: SEQUENCE; Schema: public; Owner: martu9
--

CREATE SEQUENCE productlist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE productlist_id_seq OWNER TO martu9;

--
-- Name: productlist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: martu9
--

ALTER SEQUENCE productlist_id_seq OWNED BY productlist.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: martu9
--

ALTER TABLE ONLY adminlogin ALTER COLUMN id SET DEFAULT nextval('adminlogin_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: martu9
--

ALTER TABLE ONLY productlist ALTER COLUMN id SET DEFAULT nextval('productlist_id_seq'::regclass);


--
-- Data for Name: adminlogin; Type: TABLE DATA; Schema: public; Owner: martu9
--

COPY adminlogin (id, username, password) FROM stdin;
1	admin	admin6
\.


--
-- Name: adminlogin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: martu9
--

SELECT pg_catalog.setval('adminlogin_id_seq', 1, false);


--
-- Data for Name: productlist; Type: TABLE DATA; Schema: public; Owner: martu9
--

COPY productlist (id, product_id, category) FROM stdin;
1	Resume-Arshid.doc	audi
2	364160_310_ss_01.jpg	volvo
\.


--
-- Name: productlist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: martu9
--

SELECT pg_catalog.setval('productlist_id_seq', 2, true);


--
-- Name: adminlogin_pkey; Type: CONSTRAINT; Schema: public; Owner: martu9
--

ALTER TABLE ONLY adminlogin
    ADD CONSTRAINT adminlogin_pkey PRIMARY KEY (username);


--
-- Name: productlist_pkey; Type: CONSTRAINT; Schema: public; Owner: martu9
--

ALTER TABLE ONLY productlist
    ADD CONSTRAINT productlist_pkey PRIMARY KEY (product_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

