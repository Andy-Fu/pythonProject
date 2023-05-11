from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # 设置标题
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, '互联网金融介绍', 1, 0, 'C')
        self.ln(20)

    def chapter_title(self, num, label):
        # 设置章节标题
        self.set_font('Arial', '', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, f'Chapter {num}: {label}', 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, content):
        # 添加章节内容
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, content)
        self.ln()

    def print_chapter(self, num, title, content):
        # 打印章节
        self.add_page()
        self.chapter_title(num, str(title).encode('utf-8'))
        self.chapter_body(str(content).encode('utf-8'))

pdf = PDF()
pdf.add_font('siyuan','',r"C:\Users\usr\AppData\Local\Microsoft\Windows\Fonts\SourceHanSansSC-VF.ttf",True)
pdf.set_font('siyuan', '', 100)
pdf.print_chapter(1, '什么是互联网金融？',
                  '互联网金融是指利用互联网技术进行金融业务活动的一种模式。'
                  '它在传统金融模式基础上，利用大数据、人工智能、区块链等新技术，'
                  '通过互联网实现金融产品的设计、生产、销售、交易等业务活动。')

pdf.print_chapter(2, '互联网金融的发展历程',
                  '互联网金融起源于2005年的美国，随着技术的不断进步和应用场景的拓展，'
                  '互联网金融在全球范围内得到了迅速的发展。我国的互联网金融则始于2007年，'
                  '经过多年的发展，已成为我国金融体系的重要组成部分。')

pdf.print_chapter(3, '互联网金融的特点',
                  '互联网金融具有以下特点：1.便捷快速，用户可以通过互联网轻松获取金融服务；'
                  '2.风险高效管理，利用大数据和人工智能等技术对风险进行预测和控制；'
                  '3.创新性强，通过新技术的应用，开发出各种新型金融产品。')

pdf.output('internet_finance.pdf', 'F')
