/*!
 * Complemento de validación de jQuery 1.11.1
 *
 * http://bassistance.de/jquery-plugins/jquery-plugin-validation/
 * http://docs.jquery.com/Plugins/Validation
 *
 * Copyright 2013 Jörn Zaefferer
 * Publicado bajo la licencia MIT:
 * http://www.opensource.org/licenses/mit-license.php
 */

(función ($) {

$ .extend ($. fn, {
	// http://docs.jquery.com/Plugins/Validation/validate
	validar: función (opciones) {

		// si no se selecciona nada, no devuelve nada; no puedo encadenar de todos modos
		if (! this.length) {
			if (opciones && options.debug && window.console) {
				console.warn ("Nada seleccionado, no se puede validar, no devuelve nada.");
			}
			regreso;
		}

		// comprobar si ya se ha creado un validador para este formulario
		var validador = $ .data (este [0], "validador");
		if (validador) {
			validador de retorno;
		}

		// Agrega la etiqueta novalidate si es HTML5.
		this.attr ("novalidate", "novalidate");

		validador = nuevo $ .validator (opciones, este [0]);
		$ .data (este [0], "validador", validador);

		if (validator.settings.onsubmit) {

			this.validateDelegate (": enviar", "hacer clic", función (evento) {
				if (validator.settings.submitHandler) {
					validator.submitButton = event.target;
				}
				// permite suprimir la validación agregando una clase de cancelación al botón de enviar
				if ($ (event.target) .hasClass ("cancelar")) {
					validator.cancelSubmit = true;
				}

				// permite suprimir la validación agregando el atributo formnovalidate html5 al botón enviar
				if ($ (event.target) .attr ("formnovalidate")! == undefined) {
					validator.cancelSubmit = true;
				}
			});

			// valida el formulario al enviarlo
			this.submit (función (evento) {
				if (validator.settings.debug) {
					// evitar el envío del formulario para poder ver la salida de la consola
					event.preventDefault ();
				}
				function handle () {
					var oculto;
					if (validator.settings.submitHandler) {
						if (validator.submitButton) {
							// inserta una entrada oculta como reemplazo del botón de envío que falta
							hidden = $ ("<input type = 'hidden' />"). attr ("nombre", validator.submitButton.name) .val ($ (validator.submitButton) .val ()) .appendTo (validator.currentForm) ;
						}
						validator.settings.submitHandler.call (validator, validator.currentForm, evento);
						if (validator.submitButton) {
							// y limpiar después; gracias a no-block-scope, se puede hacer referencia a hidden
							hidden.remove ();
						}
						falso retorno;
					}
					devuelve verdadero;
				}

				// evitar el envío de formularios no válidos o controladores de envío personalizados
				if (validator.cancelSubmit) {
					validator.cancelSubmit = false;
					return handle ();
				}
				if (validator.form ()) {
					if (validator.pendingRequest) {
						validator.formSubmitted = true;
						falso retorno;
					}
					return handle ();
				} más {
					validator.focusInvalid ();
					falso retorno;
				}
			});
		}

		validador de retorno;
	},
	// http://docs.jquery.com/Plugins/Validation/valid
	válido: función () {
		si ($ (este [0]). es ("formulario")) {
			devuelve this.validate (). form ();
		} más {
			var válido = verdadero;
			var validador = $ (este [0] .form) .validate ();
			this.each (function () {
				válido = válido && validator.element (esto);
			});
			retorno válido;
		}
	},
	// atributos: lista de atributos separados por espacio para recuperar y eliminar
	removeAttrs: function (atributos) {
		var result = {},
			$ elemento = esto;
		$ .each (atributos.split (/ \ s /), función (índice, valor) {
			resultado [valor] = $ elemento.attr (valor);
			$ element.removeAttr (valor);
		});
		devolver resultado;
	},
	// http://docs.jquery.com/Plugins/Validation/rules
	reglas: función (comando, argumento) {
		elemento var = este [0];

		si (comando) {
			var settings = $ .data (element.form, "validador"). settings;
			var staticRules = settings.rules;
			var existingRules = $ .validator.staticRules (elemento);
			cambiar (comando) {
			caso "agregar":
				$ .extend (reglas existentes, $ .validator.normalizeRule (argumento));
				// eliminar mensajes de las reglas, pero permitir que se establezcan por separado
				eliminar existingRules.messages;
				staticRules [element.name] = existingRules;
				si (argumento.mensajes) {
					settings.messages [element.name] = $ .extend (settings.messages [element.name], argument.messages);
				}
				rotura;
			caso "eliminar":
				if (! argumento) {
					eliminar staticRules [element.name];
					return existingRules;
				}
				var filtrada = {};
				$ .each (argumento.split (/ \ s /), función (índice, método) {
					[método] filtrado = reglas existentes [método];
					eliminar reglas existentes [método];
				});
				volver filtrado;
			}
		}

		var datos = $ .validator.normalizeRules (
		$ .extend (
			{},
			$ .validator.classRules (elemento),
			$ .validator.attributeRules (elemento),
			$ .validator.dataRules (elemento),
			$ .validator.staticRules (elemento)
		), elemento);

		// asegúrese de que se requiera al frente
		if (data.required) {
			var param = data.required;
			eliminar datos requeridos;
			data = $ .extend ({required: param}, data);
		}

		devolver datos;
	}
});

// Selectores personalizados
$ .extend ($. expr [":"], {
	// http://docs.jquery.com/Plugins/Validation/blank
	en blanco: function (a) {return! $. trim ("" + $ (a) .val ()); },
	// http://docs.jquery.com/Plugins/Validation/lined
	lleno: function (a) {return !! $. trim ("" + $ (a) .val ()); },
	// http://docs.jquery.com/Plugins/Validation/unchecked
	sin marcar: function (a) {return! $ (a) .prop ("comprobado"); }
});

// constructor para validador
$ .validator = function (opciones, formulario) {
	this.settings = $ .extend (true, {}, $ .validator.defaults, opciones);
	this.currentForm = formulario;
	this.init ();
};

$ .validator.format = function (fuente, parámetros) {
	if (argumentos.longitud === 1) {
		función de retorno () {
			var args = $ .makeArray (argumentos);
			args.unshift (fuente);
			return $ .validator.format.apply (this, args);
		};
	}
	if (argumentos.longitud> 2 && params.constructor! == Array) {
		params = $ .makeArray (argumentos) .slice (1);
	}
	if (params.constructor! == Array) {
		params = [params];
	}
	$ .each (params, function (i, n) {
		source = source.replace (new RegExp ("\\ {" + i + "\\}", "g"), function () {
			return n;
		});
	});
	fuente de retorno;
};

$ .extend ($. validador, {

	valores predeterminados: {
		mensajes: {},
		grupos: {},
		reglas: {},
		errorClass: "error",
		validClass: "válido",
		errorElement: "etiqueta",
		focusInvalid: verdadero,
		errorContainer: $ ([]),
		errorLabelContainer: $ ([]),
		onsubmit: verdadero,
		ignorar: ": oculto",
		ignoreTitle: falso,
		onfocusin: function (elemento, evento) {
			this.lastActive = elemento;

			// ocultar la etiqueta de error y eliminar la clase de error en el foco si está habilitado
			if (this.settings.focusCleanup &&! this.blockFocusCleanup) {
				if (this.settings.unhighlight) {
					this.settings.unhighlight.call (this, elemento, this.settings.errorClass, this.settings.validClass);
				}
				this.addWrapper (this.errorsFor (elemento)). hide ();
			}
		},
		onfocusout: function (elemento, evento) {
			if (! this.checkable (element) && (element.name in this.submitted ||! this.optional (element))) {
				this.element (elemento);
			}
		},
		onkeyup: function (elemento, evento) {
			if (event.which === 9 && this.elementValue (element) === "") {
				regreso;
			} else if (element.name in this.submitted || element === this.lastElement) {
				this.element (elemento);
			}
		},
		onclick: function (elemento, evento) {
			// haga clic en selects, radiobuttons y checkboxes
			if (element.name in this.submitted) {
				this.element (elemento);
			}
			// o elementos de opción, marque la selección principal en ese caso
			else if (element.parentNode.name in this.submitted) {
				this.element (element.parentNode);
			}
		},
		resaltar: función (elemento, errorClass, validClass) {
			if (element.type === "radio") {
				this.findByName (element.name) .addClass (errorClass) .removeClass (validClass);
			} más {
				$ (elemento) .addClass (errorClass) .removeClass (validClass);
			}
		},
		unhighlight: function (element, errorClass, validClass) {
			if (element.type === "radio") {
				this.findByName (element.name) .removeClass (errorClass) .addClass (validClass);
			} más {
				$ (elemento) .removeClass (errorClass) .addClass (validClass);
			}
		}
	},

	// http://docs.jquery.com/Plugins/Validation/Validator/setDefaults
	setDefaults: función (configuración) {
		$ .extend ($ .validator.defaults, configuraciones);
	},

	mensajes: {
		obligatorio: "Este campo es obligatorio",
		remoto: "Corrija este campo",
		email: "Introduzca una dirección de correo electrónico válida",
		url: "Introduzca una URL válida",
		fecha: "Ingrese una fecha válida",
		dateISO: "Introduzca una fecha válida (ISO).",
		número: "Introduzca un número válido",
		dígitos: "Introduzca solo dígitos",
		tarjeta de crédito: "Ingrese un número de tarjeta de crédito válido.",
		equalTo: "Ingrese el mismo valor nuevamente.",
		maxlength: $ .validator.format ("No ingrese más de {0} caracteres"),
		minlength: $ .validator.format ("Ingrese al menos {0} caracteres"),
		rangelength: $ .validator.format ("Ingrese un valor entre {0} y {1} caracteres"),
		rango: $ .validator.format ("Ingrese un valor entre {0} y {1}."),
		max: $ .validator.format ("Ingrese un valor menor o igual que {0}."),
		min: $ .validator.format ("Ingrese un valor mayor o igual que {0}.")
	},

	autoCreateRanges: falso,

	prototipo: {

		init: function () {
			this.labelContainer = $ (this.settings.errorLabelContainer);
			this.errorContext = this.labelContainer.length && this.labelContainer || $ (this.currentForm);
			this.containers = $ (this.settings.errorContainer) .add (this.settings.errorLabelContainer);
			this.submitted = {};
			this.valueCache = {};
			this.pendingRequest = 0;
			this.pending = {};
			this.invalid = {};
			this.reset ();

			var grupos = (this.groups = {});
			$ .each (this.settings.groups, function (key, value) {
				if (typeof value === "string") {
					valor = valor.split (/ \ s /);
				}
				$ .each (valor, función (índice, nombre) {
					grupos [nombre] = clave;
				});
			});
			var rules = this.settings.rules;
			$ .each (reglas, función (clave, valor) {
				reglas [clave] = $ .validator.normalizeRule (valor);
			});

			función delegado (evento) {
				var validador = $ .data (este [0] .form, "validador"),
					eventType = "en" + event.type.replace (/ ^ validar /, "");
				if (validator.settings [eventType]) {
					validator.settings [eventType] .call (validador, este [0], evento);
				}
			}
			$ (this.currentForm)
				.validateDelegate (": texto, [tipo = 'contraseña'], [tipo = 'archivo'], seleccionar, área de texto," +
					"[tipo = 'número'], [tipo = 'búsqueda'], [tipo = 'tel'], [tipo = 'url']," +
					"[tipo = 'correo electrónico'], [tipo = 'fecha y hora'], [tipo = 'fecha'], [tipo = 'mes']," +
					"[tipo = 'semana'], [tipo = 'hora'], [tipo = 'fecha y hora-local']," +
					"[tipo = 'rango'], [tipo = 'color']",
					"focusin focusout keyup", delegado)
				.validateDelegate ("[type = 'radio'], [type = 'checkbox'], select, option", "click", delegate);

			if (this.settings.invalidHandler) {
				$ (this.currentForm) .bind ("formulario-inválido.validate", this.settings.invalidHandler);
			}
		},

		// http://docs.jquery.com/Plugins/Validation/Validator/form
		formulario: función () {
			this.checkForm ();
			$ .extend (esto.enviado, this.errorMap);
			this.invalid = $ .extend ({}, this.errorMap);
			if (! this.valid ()) {
				$ (this.currentForm) .triggerHandler ("forma inválida", [esto]);
			}
			this.showErrors ();
			return this.valid ();
		},

		checkForm: function () {
			this.prepareForm ();
			para (var i = 0, elementos = (this.currentElements = this.elements ()); elementos [i]; i ++) {
				this.check (elementos [i]);
			}
			return this.valid ();
		},

		// http://docs.jquery.com/Plugins/Validation/Validator/element
		elemento: función (elemento) {
			element = this.validationTargetFor (this.clean (elemento));
			this.lastElement = elemento;
			this.prepareElement (elemento);
			this.currentElements = $ (elemento);
			var result = this.check (element)! == false;
			if (resultado) {
				eliminar this.invalid [element.name];
			} más {
				this.invalid [element.name] = true;
			}
			if (! this.numberOfInvalids ()) {
				// Ocultar contenedores de error en el último error
				this.toHide = this.toHide.add (este.contenedores);
			}
			this.showErrors ();
			devolver resultado;
		},

		// http://docs.jquery.com/Plugins/Validation/Validator/showErrors
		showErrors: function (errors) {
			if (errores) {
				// agregar elementos a la lista de errores y al mapa
				$ .extend (this.errorMap, errores);
				this.errorList = [];
				para (nombre de var en errores) {
					this.errorList.push ({
						mensaje: errores [nombre],
						elemento: this.findByName (nombre) [0]
					});
				}
				// eliminar elementos de la lista de éxitos
				this.successList = $ .grep (this.successList, function (element) {
					return! (element.name en errores);
				});
			}
			if (this.settings.showErrors) {
				this.settings.showErrors.call (this, this.errorMap, this.errorList);
			} más {
				this.defaultShowErrors ();
			}
		},

		// http://docs.jquery.com/Plugins/Validation/Validator/resetForm
		resetForm: function () {
			if ($ .fn.resetForm) {
				$ (this.currentForm) .resetForm ();
			}
			this.submitted = {};
			this.lastElement = null;
			this.prepareForm ();
			this.hideErrors ();
			this.elements (). removeClass (this.settings.errorClass) .removeData ("previousValue");
		},

		numberOfInvalids: function () {
			return this.objectLength (this.invalid);
		},

		objectLength: function (obj) {
			var count = 0;
			para (var i en obj) {
				contar ++;
			}
			recuento de devoluciones;
		},

		hideErrors: function () {
			this.addWrapper (this.toHide) .hide ();
		},

		válido: función () {
			devuelve this.size () === 0;
		},

		tamaño: función () {
			return this.errorList.length;
		},

		focusInvalid: function () {
			if (this.settings.focusInvalid) {
				tratar {
					$ (this.findLastActive () || this.errorList.length && this.errorList [0] .element || [])
					.filter (": visible")
					.atención()
					// activar manualmente el evento focusin; sin él, el controlador focusin no se llama, findLastActive no tendrá nada que encontrar
					.trigger ("enfocar");
				} captura (e) {
					// ignora los errores de lanzamiento de IE al enfocar elementos ocultos
				}
			}
		},

		findLastActive: function () {
			var lastActive = this.lastActive;
			return lastActive && $ .grep (this.errorList, function (n) {
				return n.element.name === lastActive.name;
			}). length === 1 && lastActive;
		},

		elementos: function () {
			var validador = esto,
				rulesCache = {};

			// seleccione todas las entradas válidas dentro del formulario (sin botones de envío o reinicio)
			return $ (this.currentForm)
			.find ("entrada, selección, área de texto")
			.not (": enviar,: restablecer,: imagen, [deshabilitado]")
			.no (esta.configuración.ignore)
			.filter (función () {
				if (! this.name && validator.settings.debug && window.console) {
					console.error ("% o no tiene un nombre asignado", esto);
				}

				// seleccione solo el primer elemento para cada nombre, y solo aquellos con reglas especificadas
				if (this.name in rulesCache ||! validator.objectLength ($ (this) .rules ())) {
					falso retorno;
				}

				rulesCache [this.name] = true;
				devuelve verdadero;
			});
		},

		clean: function (selector) {
			return $ (selector) [0];
		},

		errores: function () {
			var errorClass = this.settings.errorClass.replace ("", ".");
			return $ (this.settings.errorElement + "." + errorClass, this.errorContext);
		},

		restablecer: función () {
			this.successList = [];
			this.errorList = [];
			this.errorMap = {};
			this.toShow = $ ([]);
			this.toHide = $ ([]);
			this.currentElements = $ ([]);
		},

		prepareForm: function () {
			this.reset ();
			this.toHide = this.errors (). add (this.containers);
		},

		prepareElement: function (element) {
			this.reset ();
			this.toHide = this.errorsFor (elemento);
		},

		elementValue: function (element) {
			var tipo = $ (elemento) .attr ("tipo"),
				val = $ (elemento) .val ();

			if (escriba === "radio" || escriba === "casilla de verificación") {
				return $ ("entrada [nombre = '" + $ (elemento) .attr ("nombre") + "']: marcado"). val ();
			}

			if (typeof val === "string") {
				return val.replace (/ \ r / g, "");
			}
			return val;
		},

		comprobar: función (elemento) {
			element = this.validationTargetFor (this.clean (elemento));

			var reglas = $ (elemento) .rules ();
			var dependencyMismatch = false;
			var val = this.elementValue (elemento);
			var result;

			for (método var en reglas) {
				var regla = {método: método, parámetros: reglas [método]};
				tratar {

					resultado = $ .validator.methods [método] .call (this, val, element, rule.parameters);

					// si un método indica que el campo es opcional y por lo tanto válido,
					// no lo marque como válido cuando no haya otras reglas
					if (resultado === "desajuste de dependencia") {
						dependencyMismatch = true;
						Seguir;
					}
					dependencyMismatch = false;

					if (resultado === "pendiente") {
						this.toHide = this.toHide.not (this.errorsFor (element));
						regreso;
					}

					si (! resultado) {
						this.formatAndAdd (elemento, regla);
						falso retorno;
					}
				} captura (e) {
					if (this.settings.debug && window.console) {
						console.log ("Ocurrió una excepción al verificar el elemento" + element.id + ", verifique el método '" + rule.method + "'.", e);
					}
					lanzar e;
				}
			}
			if (dependencyMismatch) {
				regreso;
			}
			if (this.objectLength (reglas)) {
				this.successList.push (elemento);
			}
			devuelve verdadero;
		},

		// devuelve el mensaje personalizado para el elemento dado y el método de validación
		// especificado en el atributo de datos HTML5 del elemento
		customDataMessage: function (elemento, método) {
			return $ (elemento) .data ("msg-" + método.toLowerCase ()) || (element.attributes && $ (element) .attr ("data-msg-" + method.toLowerCase ()));
		},

		// devuelve el mensaje personalizado para el nombre del elemento y el método de validación dados
		customMessage: function (nombre, método) {
			var m = this.settings.messages [nombre];
			return m && (m.constructor === String? m: m [método]);
		},

		// devuelve el primer argumento definido, permitiendo cadenas vacías
		findDefined: function () {
			para (var i = 0; i <argumentos.longitud; i ++) {
				if (argumentos [i]! == indefinido) {
					devolver argumentos [i];
				}
			}
			volver indefinido;
		},

		defaultMessage: function (elemento, método) {
			devuelve this.findDefined (
				this.customMessage (element.name, método),
				this.customDataMessage (elemento, método),
				// el título nunca está indefinido, así que maneje la cadena vacía como indefinida
				! this.settings.ignoreTitle && element.title || indefinido
				$ .validator.messages [método],
				"<strong> Advertencia: no se ha definido ningún mensaje para" + element.name + "</strong>"
			);
		},

		formatAndAdd: function (elemento, regla) {
			var message = this.defaultMessage (elemento, rule.method),
				theregex = / \ $? \ {(\ d +) \} / g;
			if (tipo de mensaje === "función") {
				message = message.call (this, rule.parameters, element);
			} else if (theregex.test (mensaje)) {
				message = $ .validator.format (message.replace (theregex, "{$ 1}"), rule.parameters);
			}
			this.errorList.push ({
				mensaje: mensaje,
				elemento: elemento
			});

			this.errorMap [element.name] = mensaje;
			this.submitted [element.name] = mensaje;
		},

		addWrapper: function (toToggle) {
			if (this.settings.wrapper) {
				toToggle = toToggle.add (toToggle.parent (this.settings.wrapper));
			}
			volver a Cambiar;
		},

		defaultShowErrors: function () {
			var i, elementos;
			para (i = 0; this.errorList [i]; i ++) {
				var error = this.errorList [i];
				if (this.settings.highlight) {
					this.settings.highlight.call (this, error.element, this.settings.errorClass, this.settings.validClass);
				}
				this.showLabel (error.element, error.message);
			}
			if (this.errorList.length) {
				this.toShow = this.toShow.add (este.contenedores);
			}
			if (this.settings.success) {
				para (i = 0; this.successList [i]; i ++) {
					this.showLabel (this.successList [i]);
				}
			}
			if (this.settings.unhighlight) {
				para (i = 0, elementos = this.validElements (); elementos [i]; i ++) {
					this.settings.unhighlight.call (this, elementos [i], this.settings.errorClass, this.settings.validClass);
				}
			}
			this.toHide = this.toHide.not (this.toShow);
			this.hideErrors ();
			this.addWrapper (this.toShow) .show ();
		},

		validElements: function () {
			devolver this.currentElements.not (this.invalidElements ());
		},

		invalidElements: function () {
			return $ (this.errorList) .map (function () {
				devuelva este.elemento;
			});
		},

		showLabel: function (elemento, mensaje) {
			var label = this.errorsFor (elemento);
			if (label.length) {
				// error de actualización / clase de éxito
				label.removeClass (this.settings.validClass) .addClass (this.settings.errorClass);
				// reemplazar el mensaje en la etiqueta existente
				label.html (mensaje);
			} más {
				// crear etiqueta
				etiqueta = $ ("<" + this.settings.errorElement + ">")
					.attr ("para", this.idOrName (elemento))
					.addClass (this.settings.errorClass)
					.html (mensaje || "");
				if (this.settings.wrapper) {
					// asegúrese de que el elemento sea visible, incluso en IE
					// mostrar realmente el elemento envuelto se maneja en otro lugar
					label = label.hide (). show (). wrap ("<" + this.settings.wrapper + "/>"). parent ();
				}
				if (! this.labelContainer.append (label) .length) {
					if (this.settings.errorPlacement) {
						this.settings.errorPlacement (etiqueta, $ (elemento));
					} más {
						label.insertAfter (elemento);
					}
				}
			}
			if (! message && this.settings.success) {
				label.text ("");
				if (typeof this.settings.success === "string") {
					label.addClass (this.settings.success);
				} más {
					this.settings.success (etiqueta, elemento);
				}
			}
			this.toShow = this.toShow.add (etiqueta);
		},

		errorsFor: function (element) {
			var name = this.idOrName (elemento);
			devuelve this.errors (). filter (function () {
				return $ (esto) .attr ("para") === nombre;
			});
		},

		idOrName: función (elemento) {
			devuelve this.groups [element.name] || (this.checkable (element)? element.name: element.id || element.name);
		},

		validationTargetFor: function (element) {
			// si es radio / checkbox, valida el primer elemento del grupo en su lugar
			if (this.checkable (element)) {
				element = this.findByName (element.name) .not (this.settings.ignore) [0];
			}
			elemento de retorno;
		},

		comprobable: función (elemento) {
			return (/radio|checkbox/i).test(element.type);
		},

		findByName: function (nombre) {
			return $ (this.currentForm) .find ("[nombre = '" + nombre + "']");
		},

		getLength: function (value, element) {
			switch (element.nodeName.toLowerCase ()) {
			caso "seleccionar":
				return $ ("opción: seleccionado", elemento) .length;
			caso "entrada":
				if (this.checkable (element)) {
					return this.findByName (element.name) .filter (": comprobado"). length;
				}
			}
			return value.length;
		},

		dependen: function (param, element) {
			devolver this.dependTypes [typeof param]? this.dependTypes [tipo de parámetro] (parámetro, elemento): verdadero;
		},

		dependTypes: {
			"booleano": función (parámetro, elemento) {
				return param;
			},
			"cadena": función (parámetro, elemento) {
				return !! $ (param, element.form) .length;
			},
			"función": función (parámetro, elemento) {
				return param (elemento);
			}
		},

		opcional: función (elemento) {
			var val = this.elementValue (elemento);
			return! $. validator.methods.required.call (this, val, element) && "dependencia-desajuste";
		},

		startRequest: function (elemento) {
			if (! this.pending [element.name]) {
				this.pendingRequest ++;
				this.pending [element.name] = true;
			}
		},

		stopRequest: function (element, valid) {
			this.pendingRequest--;
			// a veces la sincronización falla, asegúrese de que la petición pendiente nunca sea <0
			if (this.pendingRequest <0) {
				this.pendingRequest = 0;
			}
			eliminar this.pending [element.name];
			if (válido && this.pendingRequest === 0 && this.formSubmitted && this.form ()) {
				$ (this.currentForm) .submit ();
				this.formSubmitted = falso;
			} else if (! valid && this.pendingRequest === 0 && this.formSubmitted) {
				$ (this.currentForm) .triggerHandler ("forma inválida", [esto]);
				this.formSubmitted = falso;
			}
		},

		previousValue: function (element) {
			return $ .data (elemento, "previousValue") || $ .data (elemento, "previousValue", {
				antiguo: nulo,
				válido: verdadero,
				mensaje: this.defaultMessage (elemento, "remoto")
			});
		}

	},

	classRuleSettings: {
		required: {required: true},
		email: {email: true},
		url: {url: true},
		fecha: {fecha: verdadero},
		dateISO: {dateISO: true},
		número: {número: verdadero},
		dígitos: {dígitos: verdadero},
		tarjeta de crédito: {tarjeta de crédito: true}
	},

	addClassRules: function (className, reglas) {
		if (className.constructor === String) {
			this.classRuleSettings [className] = reglas;
		} más {
			$ .extend (this.classRuleSettings, className);
		}
	},

	classRules: function (elemento) {
		var reglas = {};
		var clases = $ (elemento) .attr ("clase");
		if (clases) {
			$ .each (classes.split (""), function () {
				if (esto en $ .validator.classRuleSettings) {
					$ .extend (reglas, $ .validator.classRuleSettings [esto]);
				}
			});
		}
		reglas de devolución;
	},

	attributeRules: function (element) {
		var reglas = {};
		var $ elemento = $ (elemento);
		var tipo = $ elemento [0] .getAttribute ("tipo");

		for (método var en $ .validator.methods) {
			valor var;

			// soporte para <input required> tanto en html5 como en navegadores anteriores
			if (método === "obligatorio") {
				valor = $ elemento.get (0) .getAttribute (método);
				// Algunos navegadores devuelven una cadena vacía para el atributo requerido
				// y los navegadores que no son HTML5 pueden tener marcado required = ""
				si (valor === "") {
					valor = verdadero;
				}
				// forzar a los navegadores que no son HTML5 a devolver bool
				valor = !! valor;
			} más {
				valor = $ elemento.attr (método);
			}

			// convierte el valor en un número para entradas numéricas y para texto para compatibilidad hacia atrás
			// permite que type = "date" y otros se comparen como cadenas
			if (/min|max/.test (método) && (type === null || /number|range|text/.test (type))) {
				valor = Número (valor);
			}

			if (valor) {
				reglas [método] = valor;
			} else if (escriba === método && escriba! == 'rango') {
				// excepción: el método jquery validate 'range'
				// no prueba para el tipo html5 'range'
				reglas [método] = verdadero;
			}
		}

		// maxlength se puede devolver como -1, 2147483647 (IE) y 524288 (safari) para entradas de texto
		if (rules.maxlength && /-1|2147483647|524288/.test(rules.maxlength)) {
			eliminar rules.maxlength;
		}

		reglas de devolución;
	},

	dataRules: function (elemento) {
		método var, valor,
			reglas = {}, $ elemento = $ (elemento);
		para (método en $ .validator.methods) {
			valor = $ element.data ("regla-" + método.toLowerCase ());
			if (value! == undefined) {
				reglas [método] = valor;
			}
		}
		reglas de devolución;
	},

	staticRules: function (elemento) {
		var reglas = {};
		var validador = $ .data (element.form, "validador");
		if (validator.settings.rules) {
			reglas = $ .validator.normalizeRule (validator.settings.rules [element.name]) || {};
		}
		reglas de devolución;
	},

	normalizeRules: function (reglas, elemento) {
		// manejar la verificación de dependencia
		$ .each (reglas, función (prop, val) {
			// ignora la regla cuando param es explícitamente falso, por ejemplo. requerido: falso
			si (val === falso) {
				eliminar reglas [prop];
				regreso;
			}
			if (val.param || val.depends) {
				var keepRule = true;
				switch (typeof val.depends) {
				caso "cadena":
					keepRule = !! $ (val.depends, element.form) .length;
					rotura;
				caso "función":
					keepRule = val.depends.call (elemento, elemento);
					rotura;
				}
				if (keepRule) {
					reglas [prop] = val.param! == undefined? val.param: verdadero;
				} más {
					eliminar reglas [prop];
				}
			}
		});

		// evaluar parámetros
		$ .each (reglas, función (regla, parámetro) {
			reglas [regla] = $ .isFunction (parámetro)? parámetro (elemento): parámetro;
		});

		// limpiar parámetros numéricos
		$ .each (['longitud mínima', 'longitud máxima'], función () {
			si (gobierna [esto]) {
				reglas [esto] = Número (reglas [esto]);
			}
		});
		$ .each (['rangelength', 'range'], function () {
			var partes;
			si (gobierna [esto]) {
				if ($ .isArray (gobierna [esto])) {
					reglas [esto] = [Número (reglas [esto] [0]), Número (reglas [esto] [1])];
				} else if (typeof rules [this] === "string") {
					partes = reglas [esto] .split (/ [\ s,] + /);
					reglas [esto] = [Número (partes [0]), Número (partes [1])];
				}
			}
		});

		if ($ .validator.autoCreateRanges) {
			// crear rangos automáticamente
			if (rules.min && rules.max) {
				rules.range = [rules.min, rules.max];
				eliminar rules.min;
				eliminar rules.max;
			}
			if (rules.minlength && rules.maxlength) {
				rules.rangelength = [rules.minlength, rules.maxlength];
				eliminar rules.minlength;
				eliminar rules.maxlength;
			}
		}

		reglas de devolución;
	},

	// Convierte una cadena simple en una regla {string: true}, por ejemplo, "required" a {required: true}
	normalizeRule: function (data) {
		if (tipo de datos === "cadena") {
			var transformado = {};
			$ .each (data.split (/ \ s /), function () {
				transformado [esto] = verdadero;
			});
			datos = transformados;
		}
		devolver datos;
	},

	// http://docs.jquery.com/Plugins/Validation/Validator/addMethod
	addMethod: function (nombre, método, mensaje) {
		$ .validator.methods [nombre] = método;
		$ .validator.messages [nombre] = mensaje! == indefinido? mensaje: $ .validator.messages [nombre];
		if (method.length <3) {
			$ .validator.addClassRules (nombre, $ .validator.normalizeRule (nombre));
		}
	},

	métodos: {

		// http://docs.jquery.com/Plugins/Validation/Methods/required
		requerido: función (valor, elemento, parámetro) {
			// comprobar si se cumple la dependencia
			if (! this.depend (param, element)) {
				devuelve "desajuste de dependencia";
			}
			if (element.nodeName.toLowerCase () === "seleccionar") {
				// podría ser una matriz para select-multiple o una cadena, ambos están bien de esta manera
				var val = $ (elemento) .val ();
				return val && val.length> 0;
			}
			if (this.checkable (element)) {
				devuelve this.getLength (valor, elemento)> 0;
			}
			return $ .trim (valor) .length> 0;
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/email
		correo electrónico: función (valor, elemento) {
			// contribución de Scott Gonzalez: http://projects.scottsplayground.com/email_address_validation/
			devuelve este (elemento) opcional || / ^ ((([az] | \ d | [! # \ $% & '\ * \ + \ - \ / = \? \ ^ _ `{\ |} ~] | [\ u00A0- \ uD7FF \ uF900 - \ uFDCF \ uFDF0- \ uFFEF]) + (\. ([az] | \ d | [! # \ $% & '\ * \ + \ - \ / = \? \ ^ _ `{\ |} ~ ] | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) +) *) | ((\ x22) ((((\ x20 | \ x09) * (\ x0d \ x0a))? ( \ x20 | \ x09) +)? (([\ x01- \ x08 \ x0b \ x0c \ x0e- \ x1f \ x7f] | \ x21 | [\ x23- \ x5b] | [\ x5d- \ x7e] | [ \ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) | (\\ ([\ x01- \ x09 \ x0b \ x0c \ x0d- \ x7f] | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF])))) * (((\ x20 | \ x09) * (\ x0d \ x0a))? (\ x20 | \ x09) +)? (\ x22))) @ ((([ az] | \ d | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) | (([az] | \ d | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF ]) ([az] | \ d | - | \. | _ | ~ | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) * ([az] | \ d | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]))) \.) + (([az] | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) | (([az] | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) ([az] | \ d | - | \.
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/url
		url: function (valor, elemento) {
			// contribución de Scott Gonzalez: http://projects.scottsplayground.com/iri/
			devuelve este (elemento) opcional || / ^ (https? | s? ftp): \ / \ / (((([az] | \ d | - | \. | _ | ~ | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) | (% [\ da-f] {2}) | [! \ $ & '\ (\) \ * \ +,; =] |:) * @)? (((\ d | [1 -9] \ d | 1 \ d \ d | 2 [0-4] \ d | 25 [0-5]) \. (\ D | [1-9] \ d | 1 \ d \ d | 2 [ 0-4] \ d | 25 [0-5]) \. (\ D | [1-9] \ d | 1 \ d \ d | 2 [0-4] \ d | 25 [0-5]) \. (\ d | [1-9] \ d | 1 \ d \ d | 2 [0-4] \ d | 25 [0-5])) | ((([az] | \ d | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) | (([az] | \ d | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) ([az] | \ d | - | \. | _ | ~ | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) * ([az] | \ d | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]))) \.) + (([az] | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) | (([az] | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) ([az] | \ d | - | \. | _ | ~ | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) * ([az ] | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]))) \.?) (: \ d *)?) (\ / ((([az] | \ d | - | \ . | _ | ~ | [\ u00A0- \ uD7FF \ uF900- \ uFDCF \ uFDF0- \ uFFEF]) | (% [\ da-f] {2}) | [!
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/date
		fecha: función (valor, elemento) {
			devuelve este (elemento) opcional || ! / Invalid | NaN / .test (nueva fecha (valor) .toString ());
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/dateISO
		dateISO: function (valor, elemento) {
			devuelve este (elemento) opcional || /^\d{4}[\/\-]\d{1,2}[\/\-]\d{1,2}$/.test(value);
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/number
		número: función (valor, elemento) {
			devuelve este (elemento) opcional || /^-?(?:\d+|\d{1,3}(?:,\d{3})+)?(?:\.\d+)?$/.test(value);
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/digits
		dígitos: función (valor, elemento) {
			devuelve este (elemento) opcional || /^\d+$/.test(value);
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/creditcard
		// basado en http://en.wikipedia.org/wiki/Luhn
		tarjeta de crédito: función (valor, elemento) {
			if (this.optional (element)) {
				devuelve "desajuste de dependencia";
			}
			// acepta solo espacios, dígitos y guiones
			if (/ [^ 0-9 \ -] + /. test (value)) {
				falso retorno;
			}
			var nCheck = 0,
				nDígito = 0,
				bEven = falso;

			value = value.replace (/ \ D / g, "");

			para (var n = value.length - 1; n> = 0; n--) {
				var cDigit = value.charAt (n);
				nDigit = parseInt (cDigit, 10);
				si (bEven) {
					si ((nDígito * = 2)> 9) {
						nDígito - = 9;
					}
				}
				nCheck + = nDigit;
				bEven =! bEven;
			}

			return (nCheck% 10) === 0;
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/minlength
		minlength: function (value, element, param) {
			var length = $ .isArray (valor)? value.length: this.getLength ($. trim (valor), elemento);
			devuelve este (elemento) opcional || longitud> = param;
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/maxlength
		maxlength: function (value, element, param) {
			var length = $ .isArray (valor)? value.length: this.getLength ($. trim (valor), elemento);
			devuelve este (elemento) opcional || longitud <= param;
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/rangelength
		rangelength: function (value, element, param) {
			var length = $ .isArray (valor)? value.length: this.getLength ($. trim (valor), elemento);
			devuelve este (elemento) opcional || (longitud> = param [0] && longitud <= param [1]);
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/min
		min: function (value, element, param) {
			devuelve este (elemento) opcional || valor> = param;
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/max
		max: function (value, element, param) {
			devuelve este (elemento) opcional || valor <= param;
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/range
		rango: función (valor, elemento, parámetro) {
			devuelve este (elemento) opcional || (valor> = param [0] && valor <= param [1]);
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/equalTo
		equalTo: function (value, element, param) {
			// unirse al evento de desenfoque del objetivo para revalidar cada vez que se actualiza el campo objetivo
			// TODO encuentra una manera de vincular el evento solo una vez, evitando la sobrecarga de desvinculación-revinculación
			var target = $ (param);
			if (this.settings.onfocusout) {
				target.unbind (". validate-equalTo"). bind ("blur.validate-equalTo", function () {
					$ (elemento) .valid ();
				});
			}
			valor de retorno === target.val ();
		},

		// http://docs.jquery.com/Plugins/Validation/Methods/remote
		remoto: función (valor, elemento, parámetro) {
			if (this.optional (element)) {
				devuelve "desajuste de dependencia";
			}

			var previous = this.previousValue (element);
			if (! this.settings.messages [element.name]) {
				this.settings.messages [element.name] = {};
			}
			previous.originalMessage = this.settings.messages [element.name] .remote;
			this.settings.messages [element.name] .remote = previous.message;

			param = typeof param === "cadena" && {url: param} || param;

			if (anterior.antiguo === valor) {
				volver anterior.valido;
			}

			anterior.antiguo = valor;
			var validador = esto;
			this.startRequest (elemento);
			var data = {};
			data [element.name] = valor;
			$ .ajax ($. extender (verdadero, {
				url: param,
				modo: "abortar",
				puerto: "validar" + element.name,
				dataType: "json",
				datos: datos,
				éxito: función (respuesta) {
					validator.settings.messages [element.name] .remote = previous.originalMessage;
					var válido = respuesta === verdadero || respuesta === "verdadero";
					if (válido) {
						var enviado = validator.formSubmitted;
						validator.prepareElement (elemento);
						validator.formSubmitted = enviado;
						validator.successList.push (elemento);
						eliminar validator.invalid [element.name];
						validator.showErrors ();
					} más {
						var errores = {};
						var mensaje = respuesta || validator.defaultMessage (elemento, "remoto");
						errores [element.name] = previous.message = $ .isFunction (mensaje)? mensaje (valor): mensaje;
						validator.invalid [element.name] = true;
						validator.showErrors (errores);
					}
					anterior.valido = válido;
					validator.stopRequest (elemento, válido);
				}
			}, param));
			devolver "pendiente";
		}

	}

});

// obsoleto, use $ .validator.format en su lugar
$ .format = $ .validator.format;

} (jQuery));

// modo ajax: abortar
// uso: $ .ajax ({modo: "abortar" [, puerto: "puerto único"]});
// si se usa el modo: "abortar", la solicitud anterior en ese puerto (el puerto puede ser indefinido) se cancela mediante XMLHttpRequest.abort ()
(función ($) {
	var pendientesRequests = {};
	// Use un prefiltro si está disponible (1.5+)
	if ($ .ajaxPrefilter) {
		$ .ajaxPrefilter (function (settings, _, xhr) {
			var port = settings.port;
			if (settings.mode === "abortar") {
				si (peticiones pendientes [puerto]) {
					PendientesRequests [puerto] .abort ();
				}
				peticiones pendientes [puerto] = xhr;
			}
		});
	} más {
		// Proxy ajax
		var ajax = $ .ajax;
		$ .ajax = función (configuración) {
			var mode = ("mode" en la configuración? settings: $ .ajaxSettings) .mode,
				puerto = ("puerto" en la configuración? configuración: $ .ajaxSettings) .port;
			if (modo === "abortar") {
				si (peticiones pendientes [puerto]) {
					PendientesRequests [puerto] .abort ();
				}
				PendientesRequests [puerto] = ajax.apply (esto, argumentos);
				devolver peticiones pendientes [puerto];
			}
			return ajax.apply (esto, argumentos);
		};
	}
} (jQuery));

// proporciona el complemento delegado (tipo: String, delegate: Selector, handler: Callback) para una delegación de eventos más sencilla
// handler solo se llama cuando $ (event.target) .is (delegate), en el alcance del objeto jquery para event.target
(función ($) {
	$ .extend ($. fn, {
		validateDelegate: function (delegate, type, handler) {
			return this.bind (tipo, función (evento) {
				var target = $ (event.target);
				if (target.is (delegate)) {
					return handler.apply (objetivo, argumentos);
				}
			});
		}
	});
} (jQuery));