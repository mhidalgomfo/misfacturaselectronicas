from django.db import models
from decimal import Decimal

# Create your models here.

class MiFactura(models.Model):
    uuid = models.CharField('UUID', max_length=50)
    fechaFactura = models.DateTimeField('Fecha de la factura')
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    total = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    moneda = models.CharField(max_length=50)
    nombreReceptor = models.CharField('Nombre del receptor', max_length=255)
    rfcReceptor = models.CharField('RFC del Receptor', max_length=20)
    nombreEmisor = models.CharField('Nombre del Emisor', max_length=255)
    rfcEmisor = models.CharField('RFC del Emisor', max_length=20)
    pagada = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.uuid


class Comprobante(models.Model):
    factura = models.ForeignKey(MiFactura)
    version = models.CharField(max_length=5)
    serie = models.CharField(max_length=25)
    folio = models.CharField(max_length=20)
    fecha = models.DateTimeField('Fecha del comprobante')
    sello = models.TextField()
    formaDePago = models.CharField('Forma de Pago', max_length=200)
    noCertificado = models.CharField(max_length=20)
    certificado = models.TextField()
    condicionesDePago = models.CharField(max_length=200)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    descuento = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    motivoDescuento = models.CharField(max_length=200)
    tipoCambio = models.CharField(max_length=15)
    moneda = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    tipoDeComprobante = models.CharField(max_length=200)
    metodoDePago = models.CharField(max_length=100)
    lugarExpedicion = models.CharField(max_length=200)
    numCtaPago = models.CharField(max_length=50)
    folioFiscalOrig = models.CharField(max_length=20)
    serieFolioFiscalOrig = models.CharField(max_length=25)
    fechaFolioFiscalOrig = models.DateTimeField('Fecha del comprobante Original', blank=True, null=True)
    montoFolioFiscalOrig = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))


class Emisor(models.Model):
    comprobante = models.ForeignKey(Comprobante)
    rfc = models.CharField(max_length=20)
    nombre = models.CharField(max_length=255)
    

class DomicilioFiscal(models.Model):
    emisor = models.ForeignKey(Emisor)
    calle = models.CharField(max_length=255)
    noExterior = models.CharField(max_length=255)
    noInterior = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    codigoPostal = models.CharField(max_length=10)


class ExpedidoEn(models.Model):
    emisor = models.ForeignKey(Emisor)
    calle = models.CharField(max_length=255)
    noExterior = models.CharField(max_length=255)
    noInterior = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    codigoPostal = models.CharField(max_length=10)


class Receptor(models.Model):
    comprobante = models.ForeignKey(Comprobante)
    rfc = models.CharField(max_length=20)
    nombre = models.CharField(max_length=255)


class DomicilioReceptor(models.Model):
    receptor = models.ForeignKey(Receptor)
    calle = models.CharField(max_length=255)
    noExterior = models.CharField(max_length=255)
    noInterior = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    codigoPostal = models.CharField(max_length=10)


class Conceptos(models.Model):
    comprobante = models.ForeignKey(Comprobante)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('1.00'))
    unidad = models.CharField(max_length=50)
    noIdentificacion = models.CharField(max_length=50)
    descripcion = models.TextField()
    valorUnitario = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    importe = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))


class Impuestos(models.Model):
    comprobante = models.ForeignKey(Comprobante)
    totalImpuestosRetenidos = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    totalImpuestosTrasladados = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))


class ImpuestosRetenidos(models.Model):
    impuestos = models.ForeignKey(Impuestos)
    impuesto = models.CharField(max_length=50)
    importe = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))


class ImpuestosTrasladados(models.Model):
    impuestos = models.ForeignKey(Impuestos)
    impuesto = models.CharField(max_length=50)
    tasa = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.00'))
    importe = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))


class TimbreFiscalDigital(models.Model):
    comprobante = models.ForeignKey(Comprobante)
    version = models.CharField(max_length=5)
    uuid = models.CharField(max_length=50)
    fechaTimbrado = models.DateTimeField('Fecha y hora del timbrado')
    selloCFD = models.TextField()
    noCertificadoSAT = models.CharField(max_length=20)
    selloSAT = models.TextField()
    


