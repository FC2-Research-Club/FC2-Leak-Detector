[![Codacy Badge](https://app.codacy.com/project/badge/Grade/80a9f02a029d420a938410c29cbf2b9f)](https://app.codacy.com/gh/FC2-Research-Club/FC2-Leak-Detector/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![版本](https://img.shields.io/github/v/release/FC2-Research-Club/FC2-Leak-Detector?include_prereleases&style=flat-square)](https://github.com/FC2-Research-Club/FC2-Leak-Detector/releases)
[![许可证](https://img.shields.io/badge/license-GPL--3.0-green?style=flat-square)](https://github.com/FC2-Research-Club/FC2-Leak-Detector/blob/main/LICENSE)
[![Python版本](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)](https://www.python.org/)
[![GitHub Stars](https://img.shields.io/github/stars/FC2-Research-Club/FC2-Leak-Detector?style=flat-square)](https://github.com/FC2-Research-Club/FC2-Leak-Detector/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/FC2-Research-Club/FC2-Leak-Detector?style=flat-square)](https://github.com/FC2-Research-Club/FC2-Leak-Detector/network/members)
[![CI状态](https://img.shields.io/github/actions/workflow/status/FC2-Research-Club/FC2-Leak-Detector/publish.yml?style=flat-square)](https://github.com/FC2-Research-Club/FC2-Leak-Detector/actions)
[![最后提交](https://img.shields.io/github/last-commit/FC2-Research-Club/FC2-Leak-Detector?style=flat-square)](https://github.com/FC2-Research-Club/FC2-Leak-Detector/commits/main)

# FC2流出检测器 | FC2 Leak Detector | FC2流出チェッカー

[简体中文](#简体中文) | [English](#english) | [日本語](#日本語)

## 简体中文

> [!IMPORTANT]
> **关于数据源变更与功能受限的说明 (2025.12)**
> 
> 受上游数据源 `fc2ppvdb` 2025年9月改版影响，本工具目前处于**功能受限**状态：
> 
> 1.  **数据缺失**：由于源站不再公开展示图片及部分元数据，**封面预览等关键信息目前可能无法自动抓取**。
> 2.  **网络限制**：源站已启用高强度的 Cloudflare 区域封锁（Geo-blocking），**中国大陆 IP 几乎完全无法连接**，且对VPN/代理的检测极为严格，机房网络的IP无法访问。
> 3.  **维护状态**：因为源站受到FC2官方的施压导致网站减少了展示信息并提高了鉴权，旧版“一键图文整合”的体验短期内难以恢复。建议持有**海外原生 IP** 的用户尝试使用，或等待后续适配更新。
> 
> *我们也正在关注是否有新的替代数据源出现。*

### 项目概述

FC2流出检查器是一款专业的内容状态分析工具，基于fc2ppvdb.com构建。用户只需提供某个作者的一个具体fc2视频id，即可快速获取其在fc2.com发布的作品的完整流出状态报告，同时自动整合高质量预览图和磁力链接资源。

**核心特点：**
- 强大的统计分析功能，提供直观详细的数据可视化结果
- 轻量级命令行界面设计，操作简单直观
- 丰富的自定义配置选项，满足不同场景下的分析需求

查看[完整版本更新日志](CHANGELOG.md)了解更多详情。

### 主要功能

 **视频流出状态检查** - 快速确认视频是否已经在其他网站流出  
 **作者/女优作品分析** - 分析特定作者或女优的所有视频状态  
 **批量处理** - 同时处理多个作者或女优ID  
 **磁力链接搜索** - 自动搜索并提取视频的磁力链接  
 **图片下载** - 自动下载视频缩略图  
 **详细报告生成** - 生成全面的分析报告，支持文本和JSON格式  
 **高效缓存机制** - 智能缓存减少重复请求  
 **Jellyfin元数据支持** - 为已流出视频生成Jellyfin兼容的NFO文件和海报图片

### 安装指南

#### 系统要求

- Python 3.8 或更高版本
- 支持的操作系统: Windows, macOS, Linux

#### 安装步骤

**步骤一: 安装Python**

确保您的系统已安装Python 3.8或更高版本。您可以从[Python官网](https://www.python.org/downloads/)下载并安装适合您操作系统的版本。

可以通过以下命令验证Python版本：
```bash
python --version
```

**步骤二: 获取代码**

选项1: 使用Git克隆

```bash
git clone https://github.com/FC2-Research-Club/FC2-Leak-Detector.git
cd FC2-Leak-Detector
```

选项2: 直接下载发布版本

1. 访问[GitHub Releases页面](https://github.com/FC2-Research-Club/FC2-Leak-Detector/releases)
2. 下载最新版本的源代码
3. 解压下载的文件
4. 通过命令行进入解压后的目录

**步骤三: 安装依赖**

```bash
pip install -r requirements.txt
```

### 使用方法

#### 命令行参数

```bash
python run.py [选项]

选项:
  -h, --help                显示帮助信息
  -w ID, --writer ID        分析作者ID的视频
  -a ID, --actress ID       分析女优ID的视频
  -b IDS, --batch IDS       批量处理多个作者ID (用逗号分隔)
  -ba IDS, --batch-actress  批量处理多个女优ID (用逗号分隔)
  -v ID, --video ID         通过视频ID获取作者的所有视频
  -t NUM, --threads NUM     设置并行线程数 (默认值见配置)
  --jellyfin                为已流出视频生成Jellyfin元数据（NFO文件和海报）；可单独使用，会查找48小时内的分析结果
  --no-magnet               不获取磁力链接
  --no-image                不下载视频缩略图
  -l LANG, --lang LANG      设置界面语言 (支持: zh, en, ja)
  -c, --config              显示当前配置
  -s, --sites               显示检查站点列表
  -e, --extract             提取热门作者列表
  --clear-cache             清除所有缓存数据
```

#### 示例

```bash
# 分析单个作者的作品
python run.py -w 5656

# 分析单个女优的作品
python run.py -a 5711

# 批量分析多个作者
python run.py -b 5656,3524,4461

# 批量分析多个女优
python run.py -ba 5711,3986,4219

# 通过视频ID获取作者的所有视频
python run.py -v 1234567

# 使用10个线程分析作者视频
python run.py -w 5656 -t 10

# 分析作者视频并生成Jellyfin元数据
python run.py -w 5656 --jellyfin

# 使用最近的分析结果生成Jellyfin元数据（无需重新分析）
python run.py --jellyfin

# 分析女优视频但不获取磁力链接
python run.py -a 5711 --no-magnet

# 分析作者视频但不下载缩略图
python run.py -w 5656 --no-image

# 使用英文界面
python run.py -l en

# 提取热门作者列表
python run.py -e

# 清除所有缓存
python run.py --clear-cache
```

#### 高级用法

以下是一些组合多个参数的高级用法示例：

```bash
# 使用20个线程分析作者视频，生成Jellyfin元数据，并使用英文界面
python run.py -w 5656 -t 20 --jellyfin -l en

# 批量分析多个作者，使用最大50个线程，不下载缩略图但获取磁力链接，并生成Jellyfin元数据
python run.py -b 5656,3524,4461,7890,6543,2109 -t 50 --no-image --jellyfin

# 分析女优视频，使用15个线程，不获取磁力链接，生成Jellyfin元数据，并使用日文界面
python run.py -a 5711 -t 15 --no-magnet --jellyfin -l ja

# 通过视频ID找到作者并分析其所有视频，使用30个线程，生成Jellyfin元数据
python run.py -v 1234567 -t 30 --jellyfin

# 批量分析多个女优，使用25个线程，不获取磁力链接和缩略图，生成Jellyfin元数据
python run.py -ba 5711,3986,4219,8765,5432 -t 25 --no-magnet --no-image --jellyfin

# 独立使用Jellyfin元数据生成，从最近48小时内的分析结果中选择
python run.py --jellyfin
```

> **注意**: 本项目默认语言为中文(zh)。如果您希望使用英文或日文界面，只需使用 `-l` 参数设置一次您的首选语言即可。此设置将保存在 `i18n/preference.json` 文件中，并在您更改之前的所有后续运行中使用。

### 配置说明

配置系统已更新为基于类的配置模式，使用`config.py`中的`Config`类管理所有配置项：

| 配置类别 | 参数 | 说明 | 默认值 |
|--------|------|------|--------|
| **网络请求** | max_workers | 最大并行线程数 | 30 |
| | timeout | 请求超时时间(秒) | 15 |
| | max_retries | 最大重试次数 | 4 |
| | page_interval | 分页请求间隔时间范围(秒) | (0.5, 1.2) |
| | request_interval | 普通请求间隔时间范围(秒) | (0.5, 1.0) |
| | retry_base | 重试间隔基数 | 2.0 |
| **缓存设置** | cache_ttl | 缓存有效期(秒) | 172800 (48小时) |
| **存储路径** | cache_dir | 作者和女优ID缓存目录 | data/id_cache |
| | image_dir | 视频缩略图存储目录 | data/img |
| | result_dir | 分析结果存储目录 | data/results |
| | magnet_dir | 磁链信息存储目录 | data/magnets |
| | log_dir | 日志文件存储目录 | data/logs |
| **输出设置** | save_format | 保存格式 | ["text", "json"] |
| | report_batch_size | 报告中每批显示的视频数量 | 100 |
| **高级设置** | log_level | 日志级别 | INFO |
| | enable_proxy | 是否启用代理 | false |
| | user_agents | 浏览器标识轮换列表 | [多种用户代理] |

### 目录结构

```
FC2-Leak-Detector/
├── src/                 # 源代码目录
│   ├── checkers/        # 视频检查模块
│   ├── writers/         # 作者信息模块
│   └── utils/           # 工具模块
├── data/                # 数据存储目录（自动创建）
│   ├── id_cache/        # ID缓存目录
│   ├── results/         # 结果保存目录
│   ├── img/             # 图片保存目录
│   ├── magnets/         # 磁链缓存目录
│   └── logs/            # 日志目录
├── i18n/                # 国际化语言文件
│   ├── en.json          # 英文语言文件
│   ├── ja.json          # 日文语言文件
│   └── zh.json          # 中文语言文件
├── .github/             # GitHub配置
│   └── workflows/       # GitHub工作流
├── logs/                # 根目录日志文件夹
├── run.py               # 程序入口点
├── main.py              # 主程序代码
├── config.py            # 配置文件
├── setup.py             # 包安装配置
├── requirements.txt     # 基本依赖列表
├── pyproject.toml       # 项目配置文件
├── .gitignore           # Git忽略文件
├── .editorconfig        # 编辑器配置
├── .python-version      # Python版本配置
├── CHANGELOG.md         # 更新日志
├── LICENSE              # 许可证文件
└── README.md            # 文档说明
```

### 常见问题

#### 如何找到作者ID或女优ID?

女优ID可以从fc2ppvdb.com网站的URL中找到。例如:
- 女优页面URL: `.../actress/6789` 中的 `6789` 即为女优ID
- 作者ID由于没有明文在网页中显示，用户可以选取任意一个该作者的FC2视频ID采用-v id的命令行格式直接获取该作者的视频，无需提供具体id

#### 关于Jellyfin元数据的使用

生成的Jellyfin元数据包含以下内容：
- NFO文件：包含视频标题、描述、外部链接等信息
- 海报图片：视频缩略图作为海报
- 占位MP4文件：**注意：这些是0字节的空文件，不能直接播放**，仅用于在Jellyfin中显示视频条目
- 观看链接：NFO文件中包含MissAV和123AV的观看链接，可通过预告片按钮或外部链接访问
- 磁力链接：如果可用，NFO文件中会包含磁力链接，用于下载视频

要观看视频，您需要点击Jellyfin界面中的预告片按钮跳转到在线观看网站，或使用磁力链接下载视频。

单独使用`--jellyfin`参数时，程序会查找48小时内的分析结果，并让您选择一个用于生成元数据。这样可以避免重复分析同一作者或女优的视频，方便快速生成元数据。

#### 分析速度很慢怎么办?

- 增加并行线程数 (`-t` 参数或修改配置文件中的`max_workers`值)
- 减少分析视频数量
- 确保网络连接稳定
- 禁用磁链搜索和图片下载 (`--no-magnet --no-image` 参数)

#### 为什么有些视频显示"检查失败"?

检查失败可能由以下原因导致:
- 网络连接问题
- 检查站点暂时不可用
- 请求被目标站点拒绝
- 视频ID格式不正确

#### 如何清除缓存?

手动删除 `data` 目录下的相应缓存文件夹，或使用以下命令:

```bash
python run.py --clear-cache
```

### 注意事项

1. 本工具仅用于学术研究和个人学习，请勿用于任何商业或非法用途
2. 请勿频繁大量请求，以免IP被封禁
3. 遵守相关法律法规，尊重内容版权
4. 不要分享或传播通过本工具获取的任何可能侵犯版权的内容
5. **特别提示：中国大陆用户需确保网络环境可正常访问国际互联网，以便连接本工具依赖的各项在线服务**

### 免责声明

**重要：请在使用本工具前仔细阅读以下声明**

本项目是一个技术研究工具，仅用于学术研究、数据分析和技术学习。用户必须在遵守所在地区法律法规的前提下使用本工具。本工具不提供、不存储、不分发任何版权内容，仅提供指向公开索引的元数据信息。

使用者应对自己的行为负责，作者和贡献者不对使用本工具导致的任何法律问题或损失承担责任。本工具仅用于检查内容状态，不鼓励用户获取或分享侵犯版权的内容。请尊重内容创作者的权利，支持正版内容。

本项目采用GNU通用公共许可证v3（GNU GPL v3）发布，这意味着您可以自由使用、修改和分发本软件，但需遵循GPL协议的相关规定。详细信息请参阅项目根目录下的LICENSE文件。

### Star趋势

[![Star历史图表](https://starchart.cc/FC2-Research-Club/FC2-Leak-Detector.svg)](https://starchart.cc/FC2-Research-Club/FC2-Leak-Detector)

## English

### Project Overview

FC2 Leak Detector is a professional content status analysis tool built on fc2ppvdb.com. Users only need to provide an author's specific FC2 video ID to quickly obtain a complete status report of their works published on fc2.com, while automatically integrating high-quality preview images and magnet link resources.

**Core Features:**
- Powerful statistical analysis functions, providing intuitive and detailed data visualization results
- Lightweight command-line interface design, simple and intuitive to operate
- Rich customization options to meet analysis needs in different scenarios

See the [complete changelog](CHANGELOG.md) for more details.

### Key Features

**Video Status Check** - Quickly confirm if videos have been leaked on other websites  
**Author/Actress Works Analysis** - Analyze the status of all videos by specific authors or actresses  
**Batch Processing** - Process multiple author or actress IDs simultaneously  
**Magnet Link Search** - Automatically search and extract video magnet links  
**Image Download** - Automatically download video thumbnails  
**Detailed Report Generation** - Generate comprehensive analysis reports, supporting text and JSON formats  
**Efficient Caching** - Smart caching to reduce duplicate requests  
**Jellyfin Metadata Support** - Generate Jellyfin-compatible NFO files and poster images for leaked videos

### Installation Guide

#### System Requirements

- Python 3.8 or higher
- Supported Operating Systems: Windows, macOS, Linux

#### Installation Steps

**Step 1: Install Python**

Ensure Python 3.8 or higher is installed on your system. You can download and install the appropriate version for your operating system from the [Python official website](https://www.python.org/downloads/).

You can verify your Python version with:
```bash
python --version
```

**Step 2: Get the Code**

Option 1: Using Git

```bash
git clone https://github.com/FC2-Research-Club/FC2-Leak-Detector.git
cd FC2-Leak-Detector
```

Option 2: Direct Download from Releases

1. Visit the [GitHub Releases page](https://github.com/FC2-Research-Club/FC2-Leak-Detector/releases)
2. Download the latest version source code 
3. Extract the downloaded file
4. Navigate to the extracted directory via command line

**Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### Usage

#### Command Line Arguments

```bash
python run.py [options]

Options:
  -h, --help                Show help information
  -w ID, --writer ID        Analyze videos by author ID
  -a ID, --actress ID       Analyze videos by actress ID
  -b IDS, --batch IDS       Batch process multiple author IDs (comma separated)
  -ba IDS, --batch-actress  Batch process multiple actress IDs (comma separated)
  -v ID, --video ID         Get all videos from author by video ID
  -t NUM, --threads NUM     Set parallel thread count (default in config)
  --jellyfin                Generate Jellyfin metadata (NFO files and posters) for leaked videos; can be used independently to find analysis results from the last 48 hours
  --no-magnet               Don't fetch magnet links
  --no-image                Don't download video thumbnails
  -l LANG, --lang LANG      Set interface language (supported: zh, en, ja)
  -c, --config              Show current configuration
  -s, --sites               Show check site list
  -e, --extract             Extract popular author list
  --clear-cache             Clear all cache data
```

#### Examples

```bash
# Analyze a single author's works
python run.py -w 5656

# Analyze a single actress's works
python run.py -a 5711

# Batch analyze multiple authors
python run.py -b 5656,3524,4461

# Batch analyze multiple actresses
python run.py -ba 5711,3986,4219

# Get all videos from author by video ID
python run.py -v 1234567

# Analyze author videos with 10 threads
python run.py -w 5656 -t 10

# Analyze author videos and generate Jellyfin metadata
python run.py -w 5656 --jellyfin

# Use recent analysis results to generate Jellyfin metadata (without re-analyzing)
python run.py --jellyfin

# Analyze actress videos without magnet links
python run.py -a 5711 --no-magnet

# Analyze author videos without thumbnails
python run.py -w 5656 --no-image

# Use Japanese interface
python run.py -l ja

# Extract popular author list
python run.py -e

# Clear all cache
python run.py --clear-cache
```

#### Advanced Usage

Below are some advanced usage examples combining multiple parameters:

```bash
# Use 20 threads to analyze author videos, generate Jellyfin metadata, and use English interface
python run.py -w 5656 -t 20 --jellyfin -l en

# Batch analyze multiple authors, use up to 50 threads, don't download thumbnails but fetch magnet links, and generate Jellyfin metadata
python run.py -b 5656,3524,4461,7890,6543,2109 -t 50 --no-image --jellyfin

# Analyze actress videos, use 15 threads, don't fetch magnet links, generate Jellyfin metadata, and use Japanese interface
python run.py -a 5711 -t 15 --no-magnet --jellyfin -l ja

# Find author by video ID and analyze all videos from that author, use 30 threads, and generate Jellyfin metadata
python run.py -v 1234567 -t 30 --jellyfin

# Batch analyze multiple actresses, use 25 threads, don't fetch magnet links and thumbnails, and generate Jellyfin metadata
python run.py -ba 5711,3986,4219,8765,5432 -t 25 --no-magnet --no-image --jellyfin

# Generate Jellyfin metadata independently, choosing from analysis results within the last 48 hours
python run.py --jellyfin
```

> **Note**: The default language for this project is Chinese (zh). If you prefer English or Japanese, you can use the `-l` parameter once to set your preferred language. This setting will be saved in `i18n/preference.json` and will be used for all future runs until you change it again.

### Configuration

The configuration system has been updated to a class-based model using the `Config` class in `config.py`:

| Category | Parameter | Description | Default Value |
|--------|------|------|--------|
| **Network Settings** | max_workers | Maximum parallel threads | 30 |
| | timeout | Request timeout (seconds) | 15 |
| | max_retries | Maximum retry attempts | 4 |
| | page_interval | Page request interval range (seconds) | (0.5, 1.2) |
| | request_interval | Normal request interval range (seconds) | (0.5, 1.0) |
| | retry_base | Retry interval base | 2.0 |
| **Cache Settings** | cache_ttl | Cache validity period (seconds) | 172800 (48 hours) |
| **Storage Paths** | cache_dir | ID cache directory | data/id_cache |
| | image_dir | Images save directory | data/img |
| | result_dir | Results save directory | data/results |
| | magnet_dir | Magnet cache directory | data/magnets |
| | log_dir | Log directory | data/logs |
| **Output Settings** | save_format | Save format | ["text", "json"] |
| | report_batch_size | Videos per batch in reports | 100 |
| **Advanced Settings** | log_level | Log level | INFO |
| | enable_proxy | Whether to use a proxy | false |
| | user_agents | Browser user agent rotation list | [various agents] |

### Directory Structure

```
FC2-Leak-Detector/
├── src/                 # Source code directory
│   ├── checkers/        # Video check modules
│   ├── writers/         # Author information modules
│   └── utils/           # Utility modules
├── data/                # Data storage directory (auto-created)
│   ├── id_cache/        # ID cache directory
│   ├── results/         # Results save directory
│   ├── img/             # Images save directory
│   ├── magnets/         # Magnet cache directory
│   └── logs/            # Log directory
├── i18n/                # Internationalization language files
│   ├── en.json          # English language file
│   ├── ja.json          # Japanese language file
│   └── zh.json          # Chinese language file
├── .github/             # GitHub configuration
│   └── workflows/       # GitHub workflows
├── logs/                # Root level logs directory
├── run.py               # Program entry point
├── main.py              # Main program code
├── config.py            # Configuration file
├── setup.py             # Package installation setup
├── requirements.txt     # Basic dependency list
├── pyproject.toml       # Project configuration file
├── .gitignore           # Git ignore file
├── .editorconfig        # Editor configuration
├── .python-version      # Python version configuration
├── CHANGELOG.md         # Update log
├── LICENSE              # License file
└── README.md            # Documentation
```

### FAQ

#### How to Find Author ID or Actress ID?

Actress ID can be found in the URL of fc2ppvdb.com website. For example:
- Actress page URL: `.../actress/6789` where `6789` is the actress ID
- Author ID is not explicitly displayed on the webpage. Users can select any FC2 video ID from that author and use the -v id command line format to directly get videos from that author without providing a specific id.

#### About Using Jellyfin Metadata

The generated Jellyfin metadata includes the following:
- NFO files: Contains video title, description, external links, and other information
- Poster images: Video thumbnails used as posters
- Placeholder MP4 files: **Note: These are 0-byte empty files that cannot be played directly**, only used to display video entries in Jellyfin
- Watch links: NFO files contain links to MissAV and 123AV for watching, accessible via the trailer button or external links
- Magnet links: If available, NFO files include magnet links for downloading the videos

To watch videos, you need to click the trailer button in the Jellyfin interface to jump to the online viewing website, or use the magnet link to download the video.

When using the `--jellyfin` parameter independently, the program will search for analysis results from the last 48 hours and let you choose one to generate metadata. This avoids re-analyzing the same author or actress's videos and makes it convenient to quickly generate metadata.

#### Analysis is Slow, What Should I Do?

- Increase parallel thread count (`-t` parameter or modify `max_workers` in config)
- Reduce the number of videos to analyze
- Ensure network connection is stable
- Disable magnet search and image download (`--no-magnet --no-image` parameters)

#### Why Do Some Videos Show "Check Failed"?

Check failures may be caused by:
- Network connection issues
- Check site temporarily unavailable
- Request rejected by target site
- Incorrect video ID format

#### How to Clear Cache?

Manually delete respective cache folders in the `data` directory, or use:

```bash
python run.py --clear-cache
```

### Notes

1. This tool is for academic research and personal learning only, not for any commercial or illegal purposes
2. Avoid frequent mass requests to prevent IP blocking
3. Comply with relevant laws and regulations, respect content copyright
4. Do not share or distribute any potentially copyright-infringing content obtained through this tool
5. **Important Note: Users in mainland China need to ensure proper access to the global internet to connect with online services required by this tool**

### Disclaimer

**Important: Please read the following disclaimer before using this tool**

This project is a technical research tool intended solely for academic research, data analysis, and technical learning. Users must comply with all applicable laws and regulations in their jurisdiction when using this tool. This tool does not provide, store, or distribute any copyrighted content, but only offers metadata information pointing to publicly indexed resources.

Users are responsible for their own actions. The authors and contributors are not liable for any legal issues or damages resulting from the use of this tool. This tool is intended only for checking content status and does not encourage users to obtain or share copyright-infringing content. Please respect the rights of content creators and support official content.

This project is released under the GNU General Public License v3 (GNU GPL v3), which means you are free to use, modify, and distribute this software, subject to the terms of the GPL. Please refer to the LICENSE file in the project root directory for detailed information.

### Star History

[![Star History Chart](https://starchart.cc/FC2-Research-Club/FC2-Leak-Detector.svg)](https://starchart.cc/FC2-Research-Club/FC2-Leak-Detector)

## 日本語

### プロジェクト概要

FC2流出チェッカーは、fc2ppvdb.comに基づいて構築された専門的なコンテンツステータス分析ツールです。ユーザーは、特定の作者のFC2ビデオIDを提供するだけで、fc2.comで公開されている作品の完全な流出ステータスレポートを迅速に取得でき、同時に高品質のプレビュー画像とマグネットリンク情報を自動的に統合します。

**主な特徴：**
- 強力な統計分析機能、ユーザーに直感的で詳細なデータ視覚化結果を提供
- 軽量なコマンドラインインターフェース設計、操作はシンプルで直感的
- さまざまなシナリオでの分析ニーズを満たすための豊富なカスタム設定オプション

詳細については[完全な変更履歴](CHANGELOG.md)をご覧ください。

### 主な機能

**ビデオ流出状態確認** - 動画が他のサイトに流出しているかどうかを素早く確認  
**作者/女優作品分析** - 特定の作者または女優のすべての動画状態を分析  
**バッチ処理** - 複数の作者または女優IDを同時に処理  
**マグネットリンク検索** - 動画のマグネットリンクを自動的に検索して抽出  
**画像ダウンロード** - 動画のサムネイル画像を自動的にダウンロード  
**詳細レポート生成** - テキストとJSON形式をサポートする包括的な分析レポートを生成  
**効率的なキャッシュ機構** - 重複リクエストを減らすスマートキャッシュ  
**Jellyfin メタデータサポート** - 流出したビデオ向けにJellyfin互換のNFOファイルとポスター画像を生成し、メディアライブラリーへの統合を容易にします

### インストールガイド

#### システム要件

- Python 3.8以上
- 対応OS: Windows, macOS, Linux

#### インストール手順

**ステップ1: Pythonのインストール**

システムにPython 3.8以上がインストールされていることを確認してください。[Python公式サイト](https://www.python.org/downloads/)から、お使いのOSに適したバージョンをダウンロードしてインストールできます。

以下のコマンドでPythonのバージョンを確認できます：
```bash
python --version
```

**ステップ2: コードの取得**

オプション1: Gitを使用してクローン

```bash
git clone https://github.com/FC2-Research-Club/FC2-Leak-Detector.git
cd FC2-Leak-Detector
```

オプション2: リリースから直接ダウンロード

1. [GitHubリリースページ](https://github.com/FC2-Research-Club/FC2-Leak-Detector/releases)にアクセス
2. 最新バージョンのソースコードをダウンロード
3. ダウンロードしたファイルを解凍
4. コマンドラインで解凍したディレクトリに移動

**ステップ3: 依存関係のインストール**

```bash
pip install -r requirements.txt
```

### 使用方法

#### コマンドライン引数

```bash
python run.py [オプション]

オプション:
  -h, --help                ヘルプ情報を表示
  -w ID, --writer ID        作者IDの動画を分析
  -a ID, --actress ID       女優IDの動画を分析
  -b IDS, --batch IDS       複数の作者IDをバッチ処理 (カンマ区切り)
  -ba IDS, --batch-actress  複数の女優IDをバッチ処理 (カンマ区切り)
  -v ID, --video ID         動画IDから作者のすべての動画を取得
  -t NUM, --threads NUM     並列スレッド数を設定 (設定値は設定を参照)
  --jellyfin                流出した動画のJellyfinメタデータを生成 (NFOファイルとポスター)；単独で使用可能、最近48時間の分析結果を検索
  --no-magnet               マグネットリンクを取得しない
  --no-image                動画サムネイルをダウンロードしない
  -l LANG, --lang LANG      インターフェース言語を設定 (サポート: zh, en, ja)
  -c, --config              現在の設定を表示
  -s, --sites               チェックサイトリストを表示
  -e, --extract             人気作者リストを抽出
  --clear-cache             すべてのキャッシュデータをクリア
```

#### 例

```bash
# 単一作者の作品を分析
python run.py -w 5656

# 単一女優の作品を分析
python run.py -a 5711

# 複数の作者をバッチ分析
python run.py -b 5656,3524,4461

# 複数の女優をバッチ分析
python run.py -ba 5711,3986,4219

# 動画IDから作者のすべての動画を取得
python run.py -v 1234567

# 10スレッドで作者の動画を分析
python run.py -w 5656 -t 10

# 作者の動画を分析し、Jellyfinメタデータを生成
python run.py -w 5656 --jellyfin

# 最近の分析結果からJellyfinメタデータを生成 (再分析なし)
python run.py --jellyfin

# 女優の動画を分析し、マグネットリンクを取得しない
python run.py -a 5711 --no-magnet

# 作者の動画を分析し、サムネイルをダウンロードしない
python run.py -w 5656 --no-image

# 英語インターフェースを使用
python run.py -l en

# 人気作者リストを抽出
python run.py -e

# すべてのキャッシュをクリア
python run.py --clear-cache
```

#### 高度な使用法

以下は、複数のパラメータを組み合わせた高度な使用法の例です：

```bash
# 20スレッドで作者の動画を分析し、Jellyfinメタデータを生成し、英語インターフェースを使用
python run.py -w 5656 -t 20 --jellyfin -l en

# 複数の作者をバッチ分析し、最大50スレッドを使用し、サムネイルはダウンロードせずマグネットリンクを取得し、Jellyfinメタデータを生成
python run.py -b 5656,3524,4461,7890,6543,2109 -t 50 --no-image --jellyfin

# 女優の動画を分析し、15スレッドを使用し、マグネットリンクを取得せず、Jellyfinメタデータを生成し、日本語インターフェースを使用
python run.py -a 5711 -t 15 --no-magnet --jellyfin -l ja

# 動画IDから作者を見つけ、その作者のすべての動画を分析し、30スレッドを使用し、Jellyfinメタデータを生成
python run.py -v 1234567 -t 30 --jellyfin

# 複数の女優をバッチ分析し、25スレッドを使用し、マグネットリンクとサムネイルを取得せず、Jellyfinメタデータを生成
python run.py -ba 5711,3986,4219,8765,5432 -t 25 --no-magnet --no-image --jellyfin

# Jellyfinメタデータを単独で生成し、最近48時間の分析結果から選択
python run.py --jellyfin
```

> **注意**: このプロジェクトのデフォルト言語は中国語(zh)です。英語または日本語のインターフェースを使用する場合は、`-l`パラメータを使用して一度だけ好みの言語を設定してください。この設定は`i18n/preference.json`ファイルに保存され、次回の実行まで使用されます。

### 設定説明

設定システムは、`config.py`の`Config`クラスを使用してすべての設定項目を管理するクラスベースの設定モデルに更新されました：

| 設定カテゴリ | パラメータ | 説明 | デフォルト値 |
|--------|------|------|--------|
| **ネットワークリクエスト** | max_workers | 最大並列スレッド数 | 30 |
| | timeout | リクエストタイムアウト (秒) | 15 |
| | max_retries | 最大リトライ回数 | 4 |
| | page_interval | ページリクエスト間隔範囲 (秒) | (0.5, 1.2) |
| | request_interval | 通常リクエスト間隔範囲 (秒) | (0.5, 1.0) |
| | retry_base | リトライ間隔ベース | 2.0 |
| **キャッシュ設定** | cache_ttl | キャッシュ有効期間 (秒) | 172800 (48時間) |
| **保存パス** | cache_dir | 作者と女優IDキャッシュディレクトリ | data/id_cache |
| | image_dir | 動画サムネイル保存ディレクトリ | data/img |
| | result_dir | 分析結果保存ディレクトリ | data/results |
| | magnet_dir | マグネット情報保存ディレクトリ | data/magnets |
| | log_dir | ログファイル保存ディレクトリ | data/logs |
| **出力設定** | save_format | 保存形式 | ["text", "json"] |
| | report_batch_size | レポート内の1バッチあたりの動画数 | 100 |
| **高度な設定** | log_level | ログレベル | INFO |
| | enable_proxy | プロキシを使用するかどうか | false |
| | user_agents | ブラウザユーザーエージェントローテーションリスト | [様々なエージェント] |

### ディレクトリ構造

```
FC2-Leak-Detector/
├── src/                 # ソースコードディレクトリ
│   ├── checkers/        # 動画チェックモジュール
│   ├── writers/         # 作者情報モジュール
│   └── utils/           # ユーティリティモジュール
├── data/                # データ保存ディレクトリ (自動作成)
│   ├── id_cache/        # IDキャッシュディレクトリ
│   ├── results/         # 結果保存ディレクトリ
│   ├── img/             # 画像保存ディレクトリ
│   ├── magnets/         # マグネットキャッシュディレクトリ
│   └── logs/            # ログディレクトリ
├── i18n/                # 国際化言語ファイル
│   ├── en.json          # 英語言語ファイル
│   ├── ja.json          # 日本語言語ファイル
│   └── zh.json          # 中国語言語ファイル
├── .github/             # GitHub設定
│   └── workflows/       # GitHubワークフロー
├── logs/                # ルートレベルのログディレクトリ
├── run.py               # プログラムエントリポイント
├── main.py              # メインプログラムコード
├── config.py            # 設定ファイル
├── setup.py             # パッケージインストール設定
├── requirements.txt     # 基本的な依存関係リスト
├── pyproject.toml       # プロジェクト設定ファイル
├── .gitignore           # Git無視ファイル
├── .editorconfig        # エディタ設定
├── .python-version      # Pythonバージョン設定
├── CHANGELOG.md         # 更新履歴
├── LICENSE              # ライセンスファイル
└── README.md            # ドキュメント
```

### よくある質問

#### 作者IDまたは女優IDをどうやって見つけますか？

女優IDはfc2ppvdb.comウェブサイトのURLから見つけることができます。例：
- 女優ページURL: `.../actress/6789` の `6789` が女優ID
- 作者IDはウェブページ上で明文で表示されていません。ユーザーは、その作者のFC2ビデオIDを-v idのコマンドライン形式で選択し、特定のidを提供せずにその作者の動画を直接取得できます。

#### Jellyfinメタデータの使用について

生成されたJellyfinメタデータには以下の内容が含まれています：
- NFOファイル：動画タイトル、説明、外部リンクなどの情報を含む
- ポスター画像：動画サムネイルをポスターとして使用
- プレースホルダーMP4ファイル：**注意：これらは0バイトの空ファイルで、直接再生できません**、Jellyfinで動画エントリを表示するためにのみ使用されます
- 視聴リンク：NFOファイルにはMissAVと123AVの視聴リンクが含まれ、予告映画ボタンまたは外部リンクからアクセスできます
- マグネットリンク：利用可能な場合、NFOファイルには動画をダウンロードするためのマグネットリンクが含まれます

動画を視聴するには、Jellyfinインターフェースの予告映画ボタンをクリックしてオンライン視聴サイトにジャンプするか、マグネットリンクを使用して動画をダウンロードする必要があります。

When using the `--jellyfin` parameter independently, the program will search for analysis results from the last 48 hours and let you choose one to generate metadata. This avoids re-analyzing the same author or actress's videos and makes it convenient to quickly generate metadata.

#### 分析が遅い場合はどうすればいいですか？

- 並列スレッド数を増やす (`-t`パラメータまたは設定ファイルの`max_workers`値を変更)
- 分析する動画の数を減らす
- ネットワーク接続が安定していることを確認する
- マグネット検索と画像ダウンロードを無効にする (`--no-magnet --no-image`パラメータ)

#### なぜいくつかの動画に"チェック失敗"と表示されるのですか？

チェック失敗は以下の原因による可能性があります：
- ネットワーク接続問題
- チェックサイトが一時的に利用できない
- 対象サイトによってリクエストが拒否された
- 動画IDの形式が正しくない

#### キャッシュをクリアするにはどうすればいいですか？

`data`ディレクトリ内の関連するキャッシュフォルダを手動で削除するか、以下のコマンドを使用します：

```bash
python run.py --clear-cache
```

### 注意事項

1. このツールは学術研究および個人学習のみに使用し、商用または非法目的には使用しないでください
2. 頻繁に大量のリクエストを行わないでください、IPがブロックされる可能性があります
3. 関連法律法規に従い、コンテンツ著作権を尊重してください
4. このツールを介して取得した潜在的に著作権侵害のコンテンツを共有または配布しないでください
5. **特別な注意：中国大陸のユーザーは、このツールが依存する各種オンラインサービスにアクセスできるように、国際インターネットへの正常なアクセスを確実に確保する必要があります**

### 免責事項

**重要：このツールを使用する前に、以下の免責事項をよく読んでください**

このプロジェクトは、学術研究、データ分析、技術学習のみを目的とした技術研究ツールです。ユーザーは、このツールを使用する際に、所在地域の法律法規に従う必要があります。このツールは、著作権コンテンツを提供、保存、配布するものではありません。公開インデックスされたリソースを指すメタデータ情報のみを提供します。

ユーザーは自身の行為に対する責任を負うものとします。作者および貢献者は、このツールの使用によって発生するいかなる法的問題または損害に対しても責任を負いません。このツールは、コンテンツステータスをチェックするためのものであり、著作権侵害のコンテンツを取得または共有することを奨励するものではありません。コンテンツクリエイターの権利を尊重し、正規コンテンツをサポートしてください。

このプロジェクトは、GNU General Public License v3 (GNU GPL v3)の下でリリースされています。これは、GPLの規定に従って、このソフトウェアを自由に使用、修正、配布できることを意味します。詳細については、プロジェクトルートディレクトリのLICENSEファイルを参照してください。

### Star履歴

[![Star履歴グラフ](https://starchart.cc/FC2-Research-Club/FC2-Leak-Detector.svg)](https://starchart.cc/FC2-Research-Club/FC2-Leak-Detector)

