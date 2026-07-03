# CLAUDE.md

Kepler Kit for Raspberry Pi Pico W — Sphinx 文档项目。

## 最近改动 (2026-07-02)

以下改动需要在其他语言分支（`docs-de`, `docs-es`, `docs-fr`, `docs-it`, `docs-ja`）中同步：

### 1. 修复 conf.py 弃用警告

**文件**: `docs/source/conf.py`

移除了已弃用的 `html_theme_path` 配置行：

```python
# 旧（已弃用，会导致构建报错）
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# 新
html_theme = 'sphinx_rtd_theme'
```

### 2. "18650 Battery" → "Power Pack"

全文搜索替换，共涉及 **14 个文件**：

- `docs/source/cproject/ar_motor.rst`
- `docs/source/cproject/ar_pump.rst`
- `docs/source/piperproject/2.12_smart_fan.rst`
- `docs/source/pyproject/py_motor.rst`
- `docs/source/pyproject/py_pump.rst`
- `docs/source/pyproject/iotproject/2.cheerlight.rst`
- `docs/source/pyproject/iotproject/3.ifttt_mail.rst`
- `docs/source/pyproject/iotproject/4.openweather.rst`
- `docs/source/pyproject/iotproject/5.mqtt_pub.rst`
- `docs/source/pyproject/iotproject/6.mqtt_sub.rst`
- `docs/source/pyproject/iotproject/7.web_page.rst`
- `docs/source/pyproject/iotproject/8.anvil.rst`
- `docs/source/pyproject/iotproject/9.sunfounder_controller.rst`
- `docs/source/pyproject/iotproject/10.plant_monitor.rst`

替换内容：`18650 Battery` → `Power Pack`（精确匹配，区分大小写）

### 3. "18650" → "Power Pack"

**文件**: `docs/source/component/component_lipo_charger.rst`

原文：`an 800mAh 18650 used together` → `an 800mAh Power Pack used together`

### 同步到其他分支的方法

对每个语言分支执行：

```bash
# 1. 修复 conf.py — 移除 html_theme_path 行
# 手动编辑 conf.py，删除含有 get_html_theme_path() 的那一行

# 2. 全文替换
cd docs/source
grep -rl "18650 Battery" . | xargs sed -i 's/18650 Battery/Power Pack/g'
grep -rl "18650" . | xargs sed -i 's/18650/Power Pack/g'
```
