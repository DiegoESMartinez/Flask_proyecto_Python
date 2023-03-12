-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-03-2023 a las 23:25:23
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `api_personajes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especies`
--

CREATE TABLE `especies` (
  `ID` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `especies`
--

INSERT INTO `especies` (`ID`, `nombre`, `descripcion`) VALUES
(2, 'criptoniano', 'cositas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generos`
--

CREATE TABLE `generos` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `generos`
--

INSERT INTO `generos` (`ID`, `Nombre`, `Descripcion`) VALUES
(2, 'Mujer', 'Le palé');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localizaciones`
--

CREATE TABLE `localizaciones` (
  `ID` int(11) NOT NULL,
  `Coordenadas` varchar(150) NOT NULL,
  `Ciudad` varchar(40) NOT NULL,
  `Pais` varchar(40) NOT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `Dimension` varchar(40) NOT NULL,
  `Poblacion` int(11) NOT NULL,
  `Moneda` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `localizaciones`
--

INSERT INTO `localizaciones` (`ID`, `Coordenadas`, `Ciudad`, `Pais`, `Descripcion`, `Dimension`, `Poblacion`, `Moneda`) VALUES
(1, '3242424,-523452', 'Cartagena', 'Espaliñita', 'Pais desertico e irreconocible', 'patata33', 434234, 'Bratislava'),
(5, '3242424,-523452', 'Aerzrte', 'Deutasrt', 'Pais desertico e irreconocible', 'patata33', 2147483647, 'Bratislava'),
(6, '3242424,-523452', 'Aerzrte', 'Deutasrt', 'Pais desertico e irreconocible', 'patata33', 2147483647, 'Bratislava'),
(7, '3242424,-523452', 'Aerzrte', 'Deutasrt', 'Pais desertico e irreconocible', 'Patatita', 43, 'Eurito'),
(8, '3242424,-523452', 'Aerzrte', 'Deutasrt', 'Pais desertico e irreconocible', 'Patatita', 43, 'Eurito'),
(9, '3242424,-523452', 'Aerzrte', 'Deutasrt', 'Pais desertico e irreconocible', 'Patatita', 43, 'Eurito'),
(10, '3242424,-523452', 'Aerzrte', 'Deutasrt', 'Pais desertico e irreconocible', 'ss', 43, 'Eurito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personajes`
--

CREATE TABLE `personajes` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Apellidos` varchar(40) NOT NULL,
  `Edad` int(11) NOT NULL,
  `Descripcion` varchar(400) NOT NULL,
  `Padre` int(4) NOT NULL,
  `Madre` int(4) NOT NULL,
  `Especie` int(11) NOT NULL,
  `Genero` int(11) NOT NULL,
  `Imagen` varchar(255) NOT NULL,
  `Nacimiento` int(11) NOT NULL,
  `Localizacion` int(11) NOT NULL,
  `Aparicion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personajes`
--

INSERT INTO `personajes` (`ID`, `Nombre`, `Apellidos`, `Edad`, `Descripcion`, `Padre`, `Madre`, `Especie`, `Genero`, `Imagen`, `Nacimiento`, `Localizacion`, `Aparicion`) VALUES
(8, 'Victores', 'oSSS', 44, 'accc', -1, -1, 2, 2, 'https://this-person-does-not-exist.com/gen/avatar-113fc90b9d2cb9e5f98f1e132a1dfec4.jpg', 1, 1, 1),
(14, 'Victores 2', 'oSSS', 443432, 'Personaje Random', -1, -1, 2, 2, 'https://this-person-does-not-exist.com/gen/avatar-113fc90b9d2cb9e5f98f1e132a1dfec4.jpg', 1, 1, 1),
(15, 'Victores 2', 'oSSSda', 4434324, 'Personaje Random', -1, -1, 2, 2, 'https://this-person-does-not-exist.com/gen/avatar-113fc90b9d2cb9e5f98f1e132a1dfec4.jpg', 1, 8, 1),
(17, 'Victores 2', 'oSSSda', 4434324, 'Personaje Random', -1, 15, 2, 2, 'https://this-person-does-not-exist.com/gen/avatar-113fc90b9d2cb9e5f98f1e132a1dfec4.jpg', 1, 1, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `especies`
--
ALTER TABLE `especies`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `generos`
--
ALTER TABLE `generos`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `localizaciones`
--
ALTER TABLE `localizaciones`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `personajes`
--
ALTER TABLE `personajes`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID` (`Localizacion`),
  ADD KEY `ID2` (`Aparicion`),
  ADD KEY `Nacimiento` (`Nacimiento`),
  ADD KEY `Localizacion` (`Localizacion`),
  ADD KEY `Aparicion` (`Aparicion`),
  ADD KEY `Especie` (`Especie`),
  ADD KEY `Genero` (`Genero`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `especies`
--
ALTER TABLE `especies`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `generos`
--
ALTER TABLE `generos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `localizaciones`
--
ALTER TABLE `localizaciones`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `personajes`
--
ALTER TABLE `personajes`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `personajes`
--
ALTER TABLE `personajes`
  ADD CONSTRAINT `personajes_ibfk_1` FOREIGN KEY (`Especie`) REFERENCES `especies` (`ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `personajes_ibfk_2` FOREIGN KEY (`Nacimiento`) REFERENCES `localizaciones` (`ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `personajes_ibfk_3` FOREIGN KEY (`Localizacion`) REFERENCES `localizaciones` (`ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `personajes_ibfk_4` FOREIGN KEY (`Aparicion`) REFERENCES `localizaciones` (`ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `personajes_ibfk_5` FOREIGN KEY (`Genero`) REFERENCES `generos` (`ID`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
