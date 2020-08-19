-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 03 Haz 2020, 23:04:55
-- Sunucu sürümü: 10.4.8-MariaDB
-- PHP Sürümü: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `ktuveritabani`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `gorevliler`
--

CREATE TABLE `gorevliler` (
  `id` int(11) NOT NULL,
  `ad` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `soyad` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `telefon` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `eposta` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `parola` varchar(12) COLLATE utf8_turkish_ci DEFAULT NULL,
  `adres` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `gorevliler`
--

INSERT INTO `gorevliler` (`id`, `ad`, `soyad`, `telefon`, `eposta`, `parola`, `adres`) VALUES
(1, 'mert', 'kısa', '55555555555', 'mert@mail.com', 'mert12345', 'karadeniz teknik üniversitesi'),
(2, 'hasan', 'kılıç', '55555555555', 'hasan@mail.com', 'hasan12345', 'trabzon');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kitaplar`
--

CREATE TABLE `kitaplar` (
  `id` int(11) NOT NULL,
  `barkodno` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `kitapad` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `yazar` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `rakam` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `raf` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `odunctarihi` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `teslimtarihi` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `alici` text COLLATE utf8_turkish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kitaplar`
--

INSERT INTO `kitaplar` (`id`, `barkodno`, `kitapad`, `yazar`, `rakam`, `raf`, `odunctarihi`, `teslimtarihi`, `alici`) VALUES
(11, '1', 'nutuk', 'mustafa kemal atatürk', '1', 'r1', '', '', NULL),
(12, '2', 'demir ökçe', 'jack london', '1', 'r1', '', '', NULL),
(13, '3', 'aşk ve gurur', 'jane austen', '1', 'r1', '', '', NULL),
(14, '4', 'uğultulu tepeler', 'emily bronte', '1', 'r1', '', '', NULL),
(15, '5', '1984', 'george orwell', '1', 'r1', '', '', NULL);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `uyeler`
--

CREATE TABLE `uyeler` (
  `id` int(11) NOT NULL,
  `tur` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `uyeno` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `ad` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `soyad` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `telefon` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `eposta` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `adres` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `hal` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL,
  `borc` varchar(250) COLLATE utf8_turkish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `uyeler`
--

INSERT INTO `uyeler` (`id`, `tur`, `uyeno`, `ad`, `soyad`, `telefon`, `eposta`, `adres`, `hal`, `borc`) VALUES
(5, 'Öğrenci', '1', 'taylan', 'çakmak', '55555555555', 'taylancakmak@mail.com', 'trabzon\n', '1', NULL),
(6, 'Sivil', '2', 'samet', 'al', '55555555555', 'sametal@mail.com', 'trabzon\n\n', '1', NULL),
(7, 'Sivil', '3', 'doğukan', 'gözaçan', '55555555555', 'dogukangozacan@mail.com', 'trabzon\n', '1', NULL);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `gorevliler`
--
ALTER TABLE `gorevliler`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kitaplar`
--
ALTER TABLE `kitaplar`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `uyeler`
--
ALTER TABLE `uyeler`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `gorevliler`
--
ALTER TABLE `gorevliler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `kitaplar`
--
ALTER TABLE `kitaplar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Tablo için AUTO_INCREMENT değeri `uyeler`
--
ALTER TABLE `uyeler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
